import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, ConstantKernel, WhiteKernel, DotProduct
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.pipeline import Pipeline
from sklearn.feature_selection import mutual_info_regression
from joblib import Parallel, delayed


# 1. 数据加载和预处理增强版
def load_and_preprocess_data(file_path):
    """加载数据并进行更健壮的预处理"""
    df = pd.read_excel(file_path)

    # 检查并处理缺失值
    if df.isnull().sum().any():
        print("发现缺失值，使用中位数填充...")
        df = df.fillna(df.median())

    # 假设前9列是输入，后6列是输出
    X = df.iloc[:, :9].values.astype(np.float64)
    y = df.iloc[:, 9:].values.astype(np.float64)

    # 检查并处理无限值
    if np.isinf(X).any() or np.isinf(y).any():
        print("发现无限值，进行替换处理...")
        X = np.nan_to_num(X, posinf=1e6, neginf=-1e6)
        y = np.nan_to_num(y, posinf=1e6, neginf=-1e6)

    # 特征重要性分析
    print("\n特征重要性分析（第一个输出变量）:")
    mi_scores = mutual_info_regression(X, y[:, 0])
    for i, score in enumerate(mi_scores):
        print(f"特征 {i + 1}: {score:.4f}")

    return X, y, df.columns[:9].tolist(), df.columns[9:].tolist()


# 2. 优化的核函数定义
def create_optimized_kernel(input_dim):
    """创建优化的复合核函数"""
    # 主RBF核（扩大参数范围）
    rbf_kernel = ConstantKernel(1.0, (1e-3, 1e3)) * RBF(
        length_scale=np.ones(input_dim),
        length_scale_bounds=(1e-5, 1e8)  # 扩大长度尺度范围
    )

    # 添加线性核和噪声核
    linear_kernel = ConstantKernel(0.1, (1e-4, 1e3)) * DotProduct()
    noise_kernel = WhiteKernel(noise_level=0.1, noise_level_bounds=(1e-5, 1e3))

    return rbf_kernel + linear_kernel + noise_kernel


# 3. 稳健的模型训练函数
def train_single_output_model(X_train, y_train, output_idx):
    """训练单个输出变量的稳健GPR模型"""
    try:
        kernel = create_optimized_kernel(X_train.shape[1])

        gpr = GaussianProcessRegressor(
            kernel=kernel,
            n_restarts_optimizer=10,
            optimizer='fmin_l_bfgs_b',
            normalize_y=True,
            random_state=42,
            alpha=1e-5
        )

        model = Pipeline([
            ('scaler', StandardScaler()),
            ('gpr', gpr)
        ])

        model.fit(X_train, y_train[:, output_idx])
        return model
    except Exception as e:
        print(f"输出 {output_idx} 训练失败: {str(e)}")
        return None


# 4.并行训练函数
def parallel_train_models(X_train, y_train, n_outputs):
    """并行训练所有输出变量的GPR模型
    参数:
        X_train: 训练集输入特征
        y_train: 训练集输出目标
        n_outputs: 输出变量数量
    返回:
        list: 训练好的模型列表
    """

    def train_single_model(X_train, y_train, output_idx):
        """训练单个输出模型"""
        try:
            kernel = create_optimized_kernel(X_train.shape[1])
            gpr = GaussianProcessRegressor(
                kernel=kernel,
                n_restarts_optimizer=10,
                optimizer='fmin_l_bfgs_b',
                normalize_y=True,
                random_state=42,
                alpha=1e-5
            )

            model = Pipeline([
                ('scaler', StandardScaler()),
                ('gpr', gpr)
            ])

            model.fit(X_train, y_train[:, output_idx])
            print(f"输出 {output_idx} 训练完成 - 最终核: {gpr.kernel_}")
            return model
        except Exception as e:
            print(f"输出 {output_idx} 训练失败: {str(e)}")
            return None

    # 并行训练所有模型
    models = Parallel(n_jobs=-1)(
        delayed(train_single_model)(X_train, y_train, i)
        for i in range(n_outputs)
    )

    return models


# 配置
data_path = r"E:\ABAQUS study\paramodle\linkage_opti\fff\LHS_1000_jisuan.xlsx"  # 替换为实际文件路径
test_size = 0.1  # 验证集比例

# 1. 数据加载和预处理
print("正在加载和预处理数据...")
X, y, input_names, output_names = load_and_preprocess_data(data_path)

# 2. 数据划分
X_train, X_val, y_train, y_val = train_test_split(
    X, y, test_size=test_size, random_state=42
)
print(f"\n数据集划分: 训练样本 {X_train.shape[0]}, 验证样本 {X_val.shape[0]}")

# 3. 并行训练所有模型
print("\n开始并行训练模型...")
models = parallel_train_models(X_train, y_train, y.shape[1])

# 4. 评估和可视化
print("\n开始评估模型...")
results = {}
n_samples = X_val.shape[0]
n_outputs = len(output_names)

# 初始化预测结果矩阵
y_pred_all = np.zeros((n_samples, n_outputs))  # 存储所有预测值
y_true_all = np.zeros((n_samples, n_outputs))  # 存储所有真实值

for i, (model, name) in enumerate(zip(models, output_names)):
    if model is None:
        continue
    # 预测
    y_pred = model.predict(X_val)
    # 保存预测值和真实值
    y_pred_all[:, i] = y_pred
    y_true_all[:, i] = y_val[:, i]
    # 计算指标
    mse = mean_squared_error(y_val[:, i], y_pred)
    r2 = r2_score(y_val[:, i], y_pred)
    results[name] = {'model': model, 'mse': mse, 'r2': r2}
    # 可视化（保持不变）
    plt.figure(figsize=(10, 6))
    plt.scatter(y_val[:, i], y_pred, alpha=0.6, label='Predicted value')
    plt.plot([y_val[:, i].min(), y_val[:, i].max()],
             [y_val[:, i].min(), y_val[:, i].max()], 'r--', label='Ideal line')
    plt.xlabel("Actual value")
    plt.ylabel("Predicted value")
    plt.title(f"{name} - Prediction (R2={r2:.3f}, MSE={mse:.3f})")
    plt.legend()
    plt.grid(True)
    plt.show()
# 将完整预测结果存入results字典
results['all_predictions'] = y_pred_all
results['all_true_values'] = y_true_all
# 保存为DataFrame便于查看（可选）
df_predictions = pd.DataFrame(
    data=np.hstack([y_true_all, y_pred_all]),
    columns=[f"True_{name}" for name in output_names] + [f"Pred_{name}" for name in output_names]
)
print("\n完整预测结果预览：")
print(df_predictions.head())

# 也可以保存到文件
df_predictions.to_csv('all_predictions.csv', index=False)
print("\n预测结果已保存到 all_predictions.csv")

# 5. 打印结果
print("\n=== 模型评估结果 ===")
avg_r2 = np.mean([v['r2'] for v in results.values()])
avg_mse = np.mean([v['mse'] for v in results.values()])

for name, metrics in results.items():
    print(f"{name}: MSE={metrics['mse']:.4f}, R2={metrics['r2']:.4f}")

print(f"\n平均性能: MSE={avg_mse:.4f}, R2={avg_r2:.4f}")

# 6. 模型保存示例
if results:
    import joblib
    first_output = next(iter(results.keys()))
    joblib.dump(results[first_output]['model'], f'gpr_model_{first_output}.joblib')
    print(f"\n已保存模型: gpr_model_{first_output}.joblib")


from deap import base, creator, tools, algorithms
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from deap import tools


# ----------------------------
# 动态定义目标权重
# ----------------------------
num_objs = len(results)
assert num_objs >= 2, "需要至少2个目标"

# 默认前 num_objs - 1 是最大化，最后一个是最小化
weights = tuple([1.0] * (num_objs - 1) + [-1.0])

# 重新注册 creator（防止重复定义报错）
if "FitnessMulti" in creator.__dict__:
    del creator.FitnessMulti
if "Individual" in creator.__dict__:
    del creator.Individual

creator.create("FitnessMulti", base.Fitness, weights=weights)
creator.create("Individual", list, fitness=creator.FitnessMulti)


# ----------------------------
# 输入变量范围
# ----------------------------
bounds = [
    (95, 170),     # Length1
    (130, 240),    # Length2
    (10, 25),      # Width1
    (10, 25),      # Width2
    (10, 20),      # Radius3
    (10, 20),      # Radius4
    (0.2, 0.8),    # r6_pos (比例，后处理)
    (5, 20),       # Depth1
    (5, 20)        # Depth2
]

num_vars = len(bounds)


# ----------------------------
# DEAP toolbox配置
# ----------------------------
toolbox = base.Toolbox()
for i, (low, up) in enumerate(bounds):
    toolbox.register(f"attr_float_{i}", random.uniform, low, up)

toolbox.register("individual", tools.initCycle, creator.Individual,
                 tuple(getattr(toolbox, f"attr_float_{i}") for i in range(num_vars)), n=1)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)


# ----------------------------
# 目标函数（调用 GPR 模型组 + 加入约束）
# ----------------------------
def predict_objectives(individual):
    x = np.array(individual).reshape(1, -1)
    length1, length2 = x[0][0], x[0][1]
    r6_pos_ratio = x[0][6]

    # 约束1：Length1 + Length2 ≤ 330
    if length1 + length2 > 330:
        return tuple([1e6] * num_objs)

    # 约束2：r6_pos ∈ [0.2, 0.8]*Length2
    if not (0.2 <= r6_pos_ratio <= 0.8):
        return tuple([1e6] * num_objs)

    # 重建 r6_pos 为绝对值
    x[0][6] = r6_pos_ratio * length2

    # 预测各目标值
    preds = [model['model'].predict(x)[0] for model in results.values()]
    return tuple(preds)

toolbox.register("evaluate", predict_objectives)
toolbox.register("mate", tools.cxSimulatedBinaryBounded, low=[b[0] for b in bounds],
                 up=[b[1] for b in bounds], eta=20.0)
toolbox.register("mutate", tools.mutPolynomialBounded, low=[b[0] for b in bounds],
                 up=[b[1] for b in bounds], eta=20.0, indpb=0.2)
toolbox.register("select", tools.selNSGA2)


# ----------------------------
# 注册目标函数统计（统计适应度的每个维度的均值、最小值、标准差）
# ----------------------------
# 只保留一个完整的统计器
stats = tools.Statistics(lambda ind: ind.fitness.values)
stats.register("avg", np.mean, axis=0)
stats.register("std", np.std, axis=0)
stats.register("min", np.min, axis=0)
stats.register("max", np.max, axis=0)


# ----------------------------
# 运行NSGA-II优化
# ----------------------------
def run_nsga_optimization():
    random.seed(42)
    pop = toolbox.population(n=300)
    ngen = 150

    pop, logbook = algorithms.eaMuPlusLambda(
        pop, toolbox,
        mu=300, lambda_=300,
        cxpb=0.9, mutpb=0.1,
        ngen=ngen,
        stats=stats,
        verbose=True
    )

    pareto = tools.sortNondominated(pop, len(pop), first_front_only=True)[0]
    print(f"\nPareto前沿个体数量: {len(pareto)}")

    obj_1_log, obj_2_log, obj_3_log = [], [], []
    for gen in range(ngen + 1):
        gen_pop = logbook[gen].get("pop", pop)
        gen_obj1, gen_obj2, gen_obj3 = [], [], []
        for ind in gen_pop:
            fit = ind.fitness.values
            gen_obj1.append(fit[0])
            gen_obj2.append(fit[1])
            gen_obj3.append(fit[2])
        obj_1_log.append(gen_obj1)
        obj_2_log.append(gen_obj2)
        obj_3_log.append(gen_obj3)

    # 保存
    pd.DataFrame(obj_1_log).to_excel("objective_1.xlsx", index_label="Generation")
    pd.DataFrame(obj_2_log).to_excel("objective_2.xlsx", index_label="Generation")
    pd.DataFrame(obj_3_log).to_excel("objective_3.xlsx", index_label="Generation")
    print("目标值演化过程保存完毕：objective_1~3.xlsx")

    return pareto, logbook


# ----------------------------
# 可视化2D或3D Pareto图
# ----------------------------
def plot_pareto_front(pareto, obj_indices=[0, 1, num_objs - 1]):
    from mpl_toolkits.mplot3d import Axes3D

    objs = np.array([ind.fitness.values for ind in pareto])

    if len(obj_indices) == 2:
        plt.figure(figsize=(8, 6))
        plt.scatter(objs[:, obj_indices[0]], objs[:, obj_indices[1]], c='blue')
        plt.xlabel(f"Obj{obj_indices[0]+1}")
        plt.ylabel(f"Obj{obj_indices[1]+1}")
        plt.title("Pareto Front (2D)")
        plt.grid(True)
        plt.show()
    elif len(obj_indices) == 3:
        fig = plt.figure(figsize=(10, 7))
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(objs[:, obj_indices[0]], objs[:, obj_indices[1]], objs[:, obj_indices[2]], c='red')
        ax.set_xlabel(f"Obj{obj_indices[0]+1}")
        ax.set_ylabel(f"Obj{obj_indices[1]+1}")
        ax.set_zlabel(f"Obj{obj_indices[2]+1}")
        plt.title("Pareto Front (3D)")
        plt.show()
    else:
        print("仅支持2D或3D可视化")


# ----------------------------
# 启动优化并可视化
# ----------------------------
if __name__ == "__main__":
    pareto_front, logbook = run_nsga_optimization()
    plot_pareto_front(pareto_front, obj_indices=[0, 1, num_objs - 1])  # 可调目标组合

    # 保存结果
    df_vars = pd.DataFrame([ind for ind in pareto_front], columns=input_names)
    df_objs = pd.DataFrame([ind.fitness.values for ind in pareto_front], columns=output_names[:num_objs])
    df_pareto = pd.concat([df_vars, df_objs], axis=1)
    df_pareto.to_excel("pareto_front_results.xlsx", index=False)
    print("已保存结果至 pareto_front_results.xlsx")
    df_log = pd.DataFrame(logbook)
    df_log.to_excel("evolution_logbook.xlsx", index=False)
    print("已保存结果至 evolution_logbook.xlsx")
