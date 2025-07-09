import os
import subprocess


def generate_inp_files():
    # 设置工作目录
    script_dir = r"E:\ABAQUS study\paramodle\linkage_opti\fff\Frequency_generated_scripts"
    output_dir = r"E:\ABAQUS study\paramodle\linkage_opti\fff\Frequency_generated_scripts\inp_files"

    # 创建输出目录
    os.makedirs(output_dir, exist_ok=True)

    # 获取所有Python脚本文件
    script_files = [f for f in os.listdir(script_dir) if f.endswith('.py')]

    # ABAQUS执行路径 (根据您的安装位置可能需要调整)
    abaqus_exec = r"D:\ABAQUS2023\commands\abaqus"

    # 批量执行脚本
    for script in script_files:
        script_path = os.path.join(script_dir, script)

        # 生成对应的inp文件名 (与脚本同名，扩展名改为.inp)
        inp_name = os.path.splitext(script)[0] + '.inp'

        # 构建ABAQUS命令
        cmd = f'"{abaqus_exec}" cae noGUI="{script_path}"'

        print(f"正在处理: {script} -> {inp_name}")
        subprocess.run(cmd, shell=True)

        # 检查生成的inp文件并移动到输出目录
        default_inp_path = os.path.join(script_dir, "abaqus.rpy")  # ABAQUS默认生成位置
        if os.path.exists(default_inp_path.replace(".rpy", ".inp")):
            os.rename(default_inp_path.replace(".rpy", ".inp"),
                      os.path.join(output_dir, inp_name))

    print(f"\n已完成! 生成的.inp文件保存在: {output_dir}")


if __name__ == "__main__":
    generate_inp_files()