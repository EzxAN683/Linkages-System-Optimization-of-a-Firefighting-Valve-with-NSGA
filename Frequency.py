from abaqus import *
from abaqusConstants import *
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()

Mdb()

import math

import os
os.chdir(r"E:\ABAQUS study\paramodle\linkage_opti")

# Define linkage parameter

length1=100.00       # ok
length2=230.00       # ok
width1=10.00         # ok
width2=10.00         # ok
radius3=15.00        # ok                # >= 10
radius4=15.00        # ok                # >= 10
r6_pos=75.00         # ok
depth1=6.00          # ok
depth2=6.00          # ok
length3=80.00-2*depth2-2*depth1
length4=80.00-2*depth2

pi=math.pi

# 1:Tilt linkage
# 2:Horizontal linkage
# 3:Short linkage
# 4:Medium linkage
#ModelName='d1='+str(depth1)+' d2='+str(depth2)+' w1='+str(width1)+' w2='+str(width2)+' L1='+str(length1)+' L2='+str(length2)+' radius3='+str(radius3)+' radius4='+str(radius4)+' r6pos='+str(r6_pos)
ModelName='L'+str(length1)+' L'+str(length2)+' w'+str(width1)+' w'+str(width2)+' r'+str(radius3)+' r'+str(radius4)+' r6p'+str(r6_pos)+' d'+str(depth1)+' d'+str(depth2)
ModelName=ModelName.replace('.','_')
mdb.Model(name=ModelName, modelType=STANDARD_EXPLICIT)


# Part

# Part1-linkage_100
s1 = mdb.models[ModelName].ConstrainedSketch(name='__profile__',
    sheetSize=600.0)
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=STANDALONE)
s1.Line(point1=(0.0, -width1/2.0), point2=(length1, -width1/2.0))
s1.HorizontalConstraint(entity=g[2], addUndoState=False)
s1.Line(point1=(0.0, width1/2.0), point2=(length1, width1/2.0))
s1.HorizontalConstraint(entity=g[3], addUndoState=False)
s1.ArcByCenterEnds(center=(0.0, 0.0), point1=(0.0, width1/2.0), point2=(0.0, -width1/2.0),
    direction=COUNTERCLOCKWISE)
s1.ArcByCenterEnds(center=(length1, 0.0), point1=(length1, width1/2.0), point2=(length1,
    -width1/2.0), direction=CLOCKWISE)
s1.CircleByCenterPerimeter(center=(0.0, 0), point1=(0.0, 3.0))
s1.CircleByCenterPerimeter(center=(length1, 0), point1=(length1, 3.0))
p = mdb.models[ModelName].Part(name='linkage_100', dimensionality=THREE_D,
    type=DEFORMABLE_BODY)
p = mdb.models[ModelName].parts['linkage_100']
p.BaseSolidExtrude(sketch=s1, depth=depth1)
s1.unsetPrimaryObject()
p = mdb.models[ModelName].parts['linkage_100']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
del mdb.models[ModelName].sketches['__profile__']

# Part2-linkage_230
s = mdb.models[ModelName].ConstrainedSketch(name='__profile__',
    sheetSize=600.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=STANDALONE)
s.Line(point1=(0.0, 0.0), point2=(length2, 0.0))
s.HorizontalConstraint(entity=g[2], addUndoState=False)
s.Line(point1=(0.0, width2), point2=(length2, width2))
s.HorizontalConstraint(entity=g[3], addUndoState=False)
s.ArcByCenterEnds(center=(0.0, width2/2.0), point1=(0.0, width2), point2=(0.0, 0.0),
    direction=COUNTERCLOCKWISE)
s.ArcByCenterEnds(center=(length2, width2/2.0), point1=(length2, width2), point2=(length2,
    0.0), direction=CLOCKWISE)
s.CircleByCenterPerimeter(center=(0.0, width2/2.0), point1=(0.0, width2/2.0-3.0))
s.CircleByCenterPerimeter(center=(length2, width2/2.0), point1=(length2, width2/2.0-3.0))
s.CircleByCenterPerimeter(center=(r6_pos, width2/2.0), point1=(r6_pos, width2/2.0-3.0))
p = mdb.models[ModelName].Part(name='linkage_230', dimensionality=THREE_D,
    type=DEFORMABLE_BODY)
p = mdb.models[ModelName].parts['linkage_230']
p.BaseSolidExtrude(sketch=s, depth=depth2)
s.unsetPrimaryObject()
p = mdb.models[ModelName].parts['linkage_230']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
del mdb.models[ModelName].sketches['__profile__']

# Part3-linkage_48
s1 = mdb.models[ModelName].ConstrainedSketch(name='__profile__',
    sheetSize=600.0)
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=STANDALONE)
s1.CircleByCenterPerimeter(center=(0.0, 0.0), point1=(0.0, radius3/2.0))
p = mdb.models[ModelName].Part(name='linkage_48', dimensionality=THREE_D,
    type=DEFORMABLE_BODY)
p = mdb.models[ModelName].parts['linkage_48']
p.BaseSolidExtrude(sketch=s1, depth=length3)
s1.unsetPrimaryObject()
p = mdb.models[ModelName].parts['linkage_48']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
del mdb.models[ModelName].sketches['__profile__']

# Part4-linkage_64
s = mdb.models[ModelName].ConstrainedSketch(name='__profile__',
    sheetSize=600.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=STANDALONE)
s.CircleByCenterPerimeter(center=(0.0, 0.0), point1=(0.0, radius4/2.0))
p = mdb.models[ModelName].Part(name='linkage_64', dimensionality=THREE_D,
    type=DEFORMABLE_BODY)
p = mdb.models[ModelName].parts['linkage_64']
p.BaseSolidExtrude(sketch=s, depth=length4)
s.unsetPrimaryObject()
p = mdb.models[ModelName].parts['linkage_64']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
del mdb.models[ModelName].sketches['__profile__']

# Part-shell_fixed
s1 = mdb.models[ModelName].ConstrainedSketch(name='__profile__',
    sheetSize=600.0)
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=STANDALONE)
session.viewports['Viewport: 1'].view.setValues(nearPlane=491.99,
    farPlane=639.381, width=891.256, height=393.085, cameraPosition=(-178.621,
    -0.13134, 565.685), cameraTarget=(-178.621, -0.13134, 0))
s1.CircleByCenterPerimeter(center=(0.0, 0.0), point1=(202.0, 0.0))
s1.CircleByCenterPerimeter(center=(0.0, 0.0), point1=(210.0, 0.0))
p = mdb.models[ModelName].Part(name='shell', dimensionality=THREE_D,
    type=DEFORMABLE_BODY)
p = mdb.models[ModelName].parts['shell']
p.BaseSolidExtrude(sketch=s1, depth=290.0)
s1.unsetPrimaryObject()
p = mdb.models[ModelName].parts['shell']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
del mdb.models[ModelName].sketches['__profile__']

# Part-box_fixed
s1 = mdb.models[ModelName].ConstrainedSketch(name='__profile__',
    sheetSize=900.0)
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=STANDALONE)
s1.rectangle(point1=(0.0, 0.0), point2=(404.0, 80.0))
s1.CircleByCenterPerimeter(center=(202.0, 40.0), point1=(0.0, 40.0))
s1.CoincidentConstraint(entity1=v[5], entity2=g[2], addUndoState=False)
s1.EqualDistanceConstraint(entity1=v[0], entity2=v[1], midpoint=v[5],
    addUndoState=False)
s1.autoTrimCurve(curve1=g[2], point1=(-0.306613922119141, 77.4107971191406))
s1.autoTrimCurve(curve1=g[3], point1=(0.937892913818359, 79.8961334228516))
s1.autoTrimCurve(curve1=g[7], point1=(-1.24000930786133, 11.5491752624512))
s1.autoTrimCurve(curve1=g[5], point1=(1.87127304077148, 0.675792694091797))
s1.autoTrimCurve(curve1=g[6], point1=(6.53818893432617, -12.682933807373))
s1.autoTrimCurve(curve1=g[11], point1=(12.7607231140137, 113.137619018555))
s1.autoTrimCurve(curve1=g[4], point1=(404.804931640625, 71.8897552490234))
s1.autoTrimCurve(curve1=g[8], point1=(402.315551757812, 79.0982513427734))
s1.autoTrimCurve(curve1=g[14], point1=(404.307067871094, 6.76475524902344))
s1.autoTrimCurve(curve1=g[9], point1=(401.817687988281, 0.550540924072266))
p = mdb.models[ModelName].Part(name='box', dimensionality=THREE_D,
    type=DEFORMABLE_BODY)
p = mdb.models[ModelName].parts['box']
p.BaseSolidExtrude(sketch=s1, depth=30.0)
s1.unsetPrimaryObject()
p = mdb.models[ModelName].parts['box']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
del mdb.models[ModelName].sketches['__profile__']
p = mdb.models[ModelName].parts['box']
f, e, d1 = p.faces, p.edges, p.datums
t = p.MakeSketchTransform(sketchPlane=f[0], sketchUpEdge=e[3],
    sketchPlaneSide=SIDE1, sketchOrientation=RIGHT, origin=(202.0, 80.0, 15.0))
s1 = mdb.models[ModelName].ConstrainedSketch(name='__profile__',
    sheetSize=818.04, gridSpacing=20.45, transform=t)
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=SUPERIMPOSE)
p = mdb.models[ModelName].parts['box']
p.projectReferencesOntoSketch(sketch=s1, filter=COPLANAR_EDGES)
s1.CircleByCenterPerimeter(center=(172.0, -5.0), point1=(172.0, -2.0))
s1.CircleByCenterPerimeter(center=(172.0-length2, -5.0), point1=(172.0-length2, -2.0))
p = mdb.models[ModelName].parts['box']
f1, e1, d2 = p.faces, p.edges, p.datums
p.CutExtrude(sketchPlane=f1[0], sketchUpEdge=e1[3], sketchPlaneSide=SIDE1,
    sketchOrientation=RIGHT, sketch=s1, flipExtrudeDirection=OFF)
s1.unsetPrimaryObject()
session.viewports['Viewport: 1'].setValues(displayedObject=p)
del mdb.models[ModelName].sketches['__profile__']



# Material
mdb.models[ModelName].Material(name='Al7075')
mdb.models[ModelName].materials['Al7075'].Density(table=((2.7E-9, ), ))
mdb.models[ModelName].materials['Al7075'].Elastic(table=((70000.0, 0.3), ))
mdb.models[ModelName].materials['Al7075'].Plastic(scaleStress=None, table=((
    250.0, 0.0), (230.0, 0.1), (260.0, 0.2), (290.0, 0.3)))
# Create section
mdb.models[ModelName].HomogeneousSolidSection(name='Solid_Al',
    material='Al7075', thickness=None)
# Assign section
p = mdb.models[ModelName].parts['box']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
region = p.Set(cells=cells, name='Set-1')
p = mdb.models[ModelName].parts['box']
p.SectionAssignment(region=region, sectionName='Solid_Al', offset=0.0,
    offsetType=MIDDLE_SURFACE, offsetField='',
    thicknessAssignment=FROM_SECTION)
p = mdb.models[ModelName].parts['linkage_48']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
region = p.Set(cells=cells, name='Set-1')
p = mdb.models[ModelName].parts['linkage_48']
p.SectionAssignment(region=region, sectionName='Solid_Al', offset=0.0,
    offsetType=MIDDLE_SURFACE, offsetField='',
    thicknessAssignment=FROM_SECTION)
p = mdb.models[ModelName].parts['linkage_64']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
region = p.Set(cells=cells, name='Set-1')
p = mdb.models[ModelName].parts['linkage_64']
p.SectionAssignment(region=region, sectionName='Solid_Al', offset=0.0,
    offsetType=MIDDLE_SURFACE, offsetField='',
    thicknessAssignment=FROM_SECTION)
p = mdb.models[ModelName].parts['linkage_100']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
region = p.Set(cells=cells, name='Set-1')
p = mdb.models[ModelName].parts['linkage_100']
p.SectionAssignment(region=region, sectionName='Solid_Al', offset=0.0,
    offsetType=MIDDLE_SURFACE, offsetField='',
    thicknessAssignment=FROM_SECTION)
p = mdb.models[ModelName].parts['linkage_230']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
region = p.Set(cells=cells, name='Set-1')
p = mdb.models[ModelName].parts['linkage_230']
p.SectionAssignment(region=region, sectionName='Solid_Al', offset=0.0,
    offsetType=MIDDLE_SURFACE, offsetField='',
    thicknessAssignment=FROM_SECTION)
p = mdb.models[ModelName].parts['shell']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
region = p.Set(cells=cells, name='Set-1')
p = mdb.models[ModelName].parts['shell']
p.SectionAssignment(region=region, sectionName='Solid_Al', offset=0.0,
    offsetType=MIDDLE_SURFACE, offsetField='',
    thicknessAssignment=FROM_SECTION)


# Assembly

# import 1*linkage_longer & 1*linkage_shorter
a1 = mdb.models[ModelName].rootAssembly
a1.DatumCsysByDefault(CARTESIAN)
p = mdb.models[ModelName].parts['linkage_100']
a1.Instance(name='linkage_100-1', part=p, dependent=ON)
p = mdb.models[ModelName].parts['linkage_230']
a1.Instance(name='linkage_230-1', part=p, dependent=ON)
a1 = mdb.models[ModelName].rootAssembly

# The instance linkage_100-1 was rotated by 64.15 degrees about the axis defined by the point 0., 7.5, 0. and the vector 0., 0., -8.
# Attention:Fixed vector with altered 100=length1
a1.rotate(instanceList=('linkage_100-1', ), axisPoint=(0.0, 0.0, 0.0),
    axisDirection=(0.0, 0.0, 8.0), angle=-math.asin(90.0/length1)*180.0/pi)

# Import 2ed linkage_shorter
a1 = mdb.models[ModelName].rootAssembly
p = mdb.models[ModelName].parts['linkage_100']
a1.Instance(name='linkage_100-2', part=p, dependent=ON)

# The instance linkage_100-2 was translated by 0., -180., 0. with respect to the assembly coordinate system
# Attention:Fixed vector
a1 = mdb.models[ModelName].rootAssembly
a1.translate(instanceList=('linkage_100-2', ), vector=(0.0, -180.0, 0.0))

# The instance linkage_100-2 was rotated by -64.15 degrees about the axis defined by the point 0., -172.5, -8. and the vector 0., 0., -8.
a1 = mdb.models[ModelName].rootAssembly
a1.rotate(instanceList=('linkage_100-2', ), axisPoint=(0.0, -180.0, 0.0),
    axisDirection=(0.0, 0.0, 8.0), angle=math.asin(90.0/length1)*180.0/pi)

# The instance linkage_100-2 was translated by 0., 0., -16. with respect to the assembly coordinate system
# Attention:Translated distance 16=depth1+depth2
a1 = mdb.models[ModelName].rootAssembly
a1.translate(instanceList=('linkage_100-2', ), vector=(0.0, 0.0, -(depth1+depth2)))

# Move linkage_longer
a1 = mdb.models[ModelName].rootAssembly
a1.translate(instanceList=('linkage_230-1', ), vector=(20.0, 0.0, 0.0))
a1 = mdb.models[ModelName].rootAssembly
e1 = a1.instances['linkage_230-1'].edges
e2 = a1.instances['linkage_100-2'].edges
a1.CoincidentPoint(movablePoint=a1.instances['linkage_230-1'].InterestingPoint(
    edge=e1[11], rule=CENTER),
    fixedPoint=a1.instances['linkage_100-2'].InterestingPoint(edge=e2[4],
    rule=CENTER))

# Linear pattern
a1 = mdb.models[ModelName].rootAssembly
# Attention:spacing1 230=length2
a1.LinearInstancePattern(instanceList=('linkage_100-2', 'linkage_100-1'),
    direction1=(1.0, 0.0, 0.0), direction2=(0.0, 1.0, 0.0), number1=2,
    number2=1, spacing1=length2, spacing2=200.038)
# Attention:spacing1 56=length3+depth1
a1 = mdb.models[ModelName].rootAssembly
a1.LinearInstancePattern(instanceList=('linkage_100-1',
    'linkage_100-1-lin-2-1'), direction1=(0.0, 0.0, 1.0), direction2=(0.0, 1.0,
    0.0), number1=2, number2=1, spacing1=length3+depth1, spacing2=110.038)
# Attention:spacing1 88=80.0+depth1
a1 = mdb.models[ModelName].rootAssembly
a1.LinearInstancePattern(instanceList=('linkage_100-2-lin-2-1',
    'linkage_100-2'), direction1=(0.0, 0.0, 1.0), direction2=(0.0, 1.0, 0.0),
    number1=2, number2=1, spacing1=80.0+depth1, spacing2=110.038)
# Attention:spacing1 72=80.0-depth2
a1 = mdb.models[ModelName].rootAssembly
a1.LinearInstancePattern(instanceList=('linkage_230-1', ), direction1=(0.0,
    0.0, 1.0), direction2=(0.0, 1.0, 0.0), number1=2, number2=1, spacing1=80.0-depth2,
    spacing2=15.0)

# Import and move box
a1 = mdb.models[ModelName].rootAssembly
p = mdb.models[ModelName].parts['box']
a1.Instance(name='box-1', part=p, dependent=ON)
# The instance box-1 was rotated by 90. degrees about the axis defined by the point 0., 0., 0. and the vector 10., 0., 0.
a1 = mdb.models[ModelName].rootAssembly
a1.rotate(instanceList=('box-1', ), axisPoint=(0.0, 0.0, 0.0), axisDirection=(
    10.0, 0.0, 0.0), angle=90.0)
# The instance box-1 was translated by 0., -170., 0. with respect to the assembly coordinate system
a1 = mdb.models[ModelName].rootAssembly
a1.translate(instanceList=('box-1', ), vector=(0.0, -170.0, 0.0))
# The instance box-1 was translated by -30., 0., 0. with respect to the assembly coordinate system
a1 = mdb.models[ModelName].rootAssembly
a1.translate(instanceList=('box-1', ), vector=(-30.0, 0.0, 0.0))
# The instance box-1 was translated by 0., 0., -8. with respect to the assembly coordinate system
# Attention:Translated distance 8=depth2
a1 = mdb.models[ModelName].rootAssembly
a1.translate(instanceList=('box-1', ), vector=(0.0, 0.0, -depth2))

# Import and move shell
a1 = mdb.models[ModelName].rootAssembly
p = mdb.models[ModelName].parts['shell']
a1.Instance(name='shell-1', part=p, dependent=ON)
# The instance shell-1 was rotated by 90. degrees about the axis defined by the point 0., 0., 0. and the vector 10., 0., 0.
a1 = mdb.models[ModelName].rootAssembly
a1.rotate(instanceList=('shell-1', ), axisPoint=(0.0, 0.0, 0.0),
    axisDirection=(10.0, 0.0, 0.0), angle=90.0)
# The instance shell-1 was translated by 0., 0., 32. with respect to the assembly coordinate system
# Attention:Translated distance 32=40.0-depth1
a1 = mdb.models[ModelName].rootAssembly
a1.translate(instanceList=('shell-1', ), vector=(0.0, 0.0, 40.0-depth2))
# The instance shell-1 was translated by 172., 0., 0. with respect to the assembly coordinate system
a1 = mdb.models[ModelName].rootAssembly
a1.translate(instanceList=('shell-1', ), vector=(172.0, 0.0, 0.0))
# The instance shell-1 was translated by 0., 30., 0. with respect to the assembly coordinate system
a1 = mdb.models[ModelName].rootAssembly
a1.translate(instanceList=('shell-1', ), vector=(0.0, 30.0, 0.0))

# Import and move linkage_64
a1 = mdb.models[ModelName].rootAssembly
p = mdb.models[ModelName].parts['linkage_64']
a1.Instance(name='linkage_64-1', part=p, dependent=ON)
# The instance linkage_64-1 was translated by 20., 0., 0. with respect to the assembly coordinate system
a1 = mdb.models[ModelName].rootAssembly
a1.translate(instanceList=('linkage_64-1', ), vector=(20.0, 0.0, 0.0))
a1 = mdb.models[ModelName].rootAssembly
e1 = a1.instances['linkage_64-1'].edges
e2 = a1.instances['linkage_230-1-lin-2-1'].edges
a1.CoincidentPoint(movablePoint=a1.instances['linkage_64-1'].InterestingPoint(
    edge=e1[0], rule=CENTER),
    fixedPoint=a1.instances['linkage_230-1-lin-2-1'].InterestingPoint(
    edge=e2[17], rule=CENTER))

# Import and move linkage_48
a1 = mdb.models[ModelName].rootAssembly
p = mdb.models[ModelName].parts['linkage_48']
a1.Instance(name='linkage_48-1', part=p, dependent=ON)
a1 = mdb.models[ModelName].rootAssembly
p = mdb.models[ModelName].parts['linkage_48']
a1.Instance(name='linkage_48-2', part=p, dependent=ON)
# CoincidentPoint
a1 = mdb.models[ModelName].rootAssembly
e11 = a1.instances['linkage_48-1'].edges
e12 = a1.instances['linkage_100-1-lin-2-1-1'].edges
a1.CoincidentPoint(movablePoint=a1.instances['linkage_48-1'].InterestingPoint(
    edge=e11[0], rule=CENTER),
    fixedPoint=a1.instances['linkage_100-1-lin-2-1-1'].InterestingPoint(
    edge=e12[6], rule=CENTER))
a1 = mdb.models[ModelName].rootAssembly
e11 = a1.instances['linkage_48-2'].edges
e12 = a1.instances['linkage_100-1-lin-2-1-lin-2-1'].edges
a1.CoincidentPoint(movablePoint=a1.instances['linkage_48-2'].InterestingPoint(
    edge=e11[0], rule=CENTER),
    fixedPoint=a1.instances['linkage_100-1-lin-2-1-lin-2-1'].InterestingPoint(
    edge=e12[6], rule=CENTER))


# Interaction-RP and coupling

# RPs-top-left
a = mdb.models[ModelName].rootAssembly
e1 = a.instances['linkage_100-1-lin-2-1-1'].edges
a.DatumPointByMidPoint(
    point1=a.instances['linkage_100-1-lin-2-1-1'].InterestingPoint(edge=e1[10],
    rule=CENTER),
    point2=a.instances['linkage_100-1-lin-2-1-1'].InterestingPoint(edge=e1[11],
    rule=CENTER))
a = mdb.models[ModelName].rootAssembly
e21 = a.instances['linkage_100-1'].edges
a.DatumPointByMidPoint(point1=a.instances['linkage_100-1'].InterestingPoint(
    edge=e21[10], rule=CENTER),
    point2=a.instances['linkage_100-1'].InterestingPoint(edge=e21[11],
    rule=CENTER))
a = mdb.models[ModelName].rootAssembly
d11 = a.datums
a.ReferencePoint(point=d11[37])
a = mdb.models[ModelName].rootAssembly
d1 = a.datums
a.ReferencePoint(point=d1[36])

# RPs-top-right
a = mdb.models[ModelName].rootAssembly
e1 = a.instances['linkage_100-1-lin-2-1'].edges
a.DatumPointByMidPoint(
    point1=a.instances['linkage_100-1-lin-2-1'].InterestingPoint(edge=e1[10],
    rule=CENTER), point2=a.instances['linkage_100-1-lin-2-1'].InterestingPoint(
    edge=e1[11], rule=CENTER))
a = mdb.models[ModelName].rootAssembly
e11 = a.instances['linkage_100-1-lin-2-1-lin-2-1'].edges
a.DatumPointByMidPoint(
    point1=a.instances['linkage_100-1-lin-2-1-lin-2-1'].InterestingPoint(
    edge=e11[10], rule=CENTER),
    point2=a.instances['linkage_100-1-lin-2-1-lin-2-1'].InterestingPoint(
    edge=e11[11], rule=CENTER))
a = mdb.models[ModelName].rootAssembly
d11 = a.datums
a.ReferencePoint(point=d11[40])
a = mdb.models[ModelName].rootAssembly
d1 = a.datums
a.ReferencePoint(point=d1[41])

# RPs-mid-left
a = mdb.models[ModelName].rootAssembly
e1 = a.instances['linkage_100-2-lin-2-1-1'].edges
a.DatumPointByMidPoint(
    point1=a.instances['linkage_100-2-lin-2-1-1'].InterestingPoint(edge=e1[4],
    rule=CENTER),
    point2=a.instances['linkage_100-2-lin-2-1-1'].InterestingPoint(edge=e1[6],
    rule=CENTER))
a = mdb.models[ModelName].rootAssembly
e21 = a.instances['linkage_100-1-lin-2-1-1'].edges
e22 = a.instances['linkage_100-2-lin-2-1-1'].edges
a.DatumPointByMidPoint(
    point1=a.instances['linkage_100-1-lin-2-1-1'].InterestingPoint(edge=e21[4],
    rule=CENTER),
    point2=a.instances['linkage_100-2-lin-2-1-1'].InterestingPoint(edge=e22[6],
    rule=CENTER))
a = mdb.models[ModelName].rootAssembly
e1 = a.instances['linkage_100-1-lin-2-1-1'].edges
a.DatumPointByMidPoint(
    point1=a.instances['linkage_100-1-lin-2-1-1'].InterestingPoint(edge=e1[4],
    rule=CENTER),
    point2=a.instances['linkage_100-1-lin-2-1-1'].InterestingPoint(edge=e1[6],
    rule=CENTER))
a = mdb.models[ModelName].rootAssembly
e21 = a.instances['linkage_100-2'].edges
e22 = a.instances['linkage_230-1'].edges
a.DatumPointByMidPoint(point1=a.instances['linkage_100-2'].InterestingPoint(
    edge=e21[6], rule=CENTER),
    point2=a.instances['linkage_230-1'].InterestingPoint(edge=e22[11],
    rule=CENTER))
a = mdb.models[ModelName].rootAssembly
e1 = a.instances['linkage_230-1'].edges
a.DatumPointByMidPoint(point1=a.instances['linkage_230-1'].InterestingPoint(
    edge=e1[11], rule=CENTER),
    point2=a.instances['linkage_230-1'].InterestingPoint(edge=e1[10],
    rule=CENTER))
a = mdb.models[ModelName].rootAssembly
e21 = a.instances['linkage_230-1'].edges
e22 = a.instances['linkage_48-2'].edges
a.DatumPointByMidPoint(point1=a.instances['linkage_230-1'].InterestingPoint(
    edge=e21[10], rule=CENTER),
    point2=a.instances['linkage_48-2'].InterestingPoint(edge=e22[1],
    rule=CENTER))
a = mdb.models[ModelName].rootAssembly
e1 = a.instances['linkage_48-1'].edges
a.DatumPointByMidPoint(point1=a.instances['linkage_48-1'].InterestingPoint(
    edge=e1[0], rule=CENTER),
    point2=a.instances['linkage_48-1'].InterestingPoint(edge=e1[1],
    rule=CENTER))
a = mdb.models[ModelName].rootAssembly
d11 = a.datums
a.ReferencePoint(point=d11[47])
a = mdb.models[ModelName].rootAssembly
d1 = a.datums
a.ReferencePoint(point=d1[48])
a = mdb.models[ModelName].rootAssembly
d11 = a.datums
a.ReferencePoint(point=d11[50])
a = mdb.models[ModelName].rootAssembly
d1 = a.datums
a.ReferencePoint(point=d1[46])
a = mdb.models[ModelName].rootAssembly
d11 = a.datums
a.ReferencePoint(point=d11[45])
a = mdb.models[ModelName].rootAssembly
d1 = a.datums
a.ReferencePoint(point=d1[44])

# RPs-mid-mid
a = mdb.models[ModelName].rootAssembly
e1 = a.instances['linkage_64-1'].edges
e2 = a.instances['linkage_230-1-lin-2-1'].edges
a.DatumPointByMidPoint(point1=a.instances['linkage_64-1'].InterestingPoint(
    edge=e1[0], rule=CENTER),
    point2=a.instances['linkage_230-1-lin-2-1'].InterestingPoint(edge=e2[16],
    rule=CENTER))
a = mdb.models[ModelName].rootAssembly
e21 = a.instances['linkage_230-1'].edges
e22 = a.instances['linkage_64-1'].edges
a.DatumPointByMidPoint(point1=a.instances['linkage_230-1'].InterestingPoint(
    edge=e21[17], rule=CENTER),
    point2=a.instances['linkage_64-1'].InterestingPoint(edge=e22[1],
    rule=CENTER))
a = mdb.models[ModelName].rootAssembly
e1 = a.instances['linkage_64-1'].edges
a.DatumPointByMidPoint(point1=a.instances['linkage_64-1'].InterestingPoint(
    edge=e1[0], rule=CENTER),
    point2=a.instances['linkage_64-1'].InterestingPoint(edge=e1[1],
    rule=CENTER))
a = mdb.models[ModelName].rootAssembly
d1 = a.datums
a.ReferencePoint(point=d1[58])
a = mdb.models[ModelName].rootAssembly
d11 = a.datums
a.ReferencePoint(point=d11[59])
a = mdb.models[ModelName].rootAssembly
d1 = a.datums
a.ReferencePoint(point=d1[57])

# RPs-mid-right
a = mdb.models[ModelName].rootAssembly
e1 = a.instances['linkage_100-2-lin-2-1-lin-2-1'].edges
a.DatumPointByMidPoint(
    point1=a.instances['linkage_100-2-lin-2-1-lin-2-1'].InterestingPoint(
    edge=e1[4], rule=CENTER),
    point2=a.instances['linkage_100-2-lin-2-1-lin-2-1'].InterestingPoint(
    edge=e1[6], rule=CENTER))
a = mdb.models[ModelName].rootAssembly
e21 = a.instances['linkage_100-1-lin-2-1-lin-2-1'].edges
e22 = a.instances['linkage_100-2-lin-2-1-lin-2-1'].edges
a.DatumPointByMidPoint(
    point1=a.instances['linkage_100-1-lin-2-1-lin-2-1'].InterestingPoint(
    edge=e21[4], rule=CENTER),
    point2=a.instances['linkage_100-2-lin-2-1-lin-2-1'].InterestingPoint(
    edge=e22[6], rule=CENTER))
a = mdb.models[ModelName].rootAssembly
e1 = a.instances['linkage_100-1-lin-2-1-lin-2-1'].edges
a.DatumPointByMidPoint(
    point1=a.instances['linkage_100-1-lin-2-1-lin-2-1'].InterestingPoint(
    edge=e1[6], rule=CENTER),
    point2=a.instances['linkage_100-1-lin-2-1-lin-2-1'].InterestingPoint(
    edge=e1[4], rule=CENTER))
a = mdb.models[ModelName].rootAssembly
e21 = a.instances['linkage_100-2-lin-2-1'].edges
e22 = a.instances['linkage_230-1'].edges
a.DatumPointByMidPoint(
    point1=a.instances['linkage_100-2-lin-2-1'].InterestingPoint(edge=e21[6],
    rule=CENTER), point2=a.instances['linkage_230-1'].InterestingPoint(
    edge=e22[6], rule=CENTER))
a = mdb.models[ModelName].rootAssembly
e1 = a.instances['linkage_230-1'].edges
e2 = a.instances['linkage_100-1-lin-2-1'].edges
a.DatumPointByMidPoint(point1=a.instances['linkage_230-1'].InterestingPoint(
    edge=e1[6], rule=CENTER),
    point2=a.instances['linkage_100-1-lin-2-1'].InterestingPoint(edge=e2[6],
    rule=CENTER))
a = mdb.models[ModelName].rootAssembly
e21 = a.instances['linkage_100-1-lin-2-1'].edges
a.DatumPointByMidPoint(
    point1=a.instances['linkage_100-1-lin-2-1'].InterestingPoint(edge=e21[4],
    rule=CENTER), point2=a.instances['linkage_100-1-lin-2-1'].InterestingPoint(
    edge=e21[6], rule=CENTER))
a = mdb.models[ModelName].rootAssembly
e21 = a.instances['linkage_100-1-lin-2-1'].edges
e22 = a.instances['linkage_48-2'].edges
a.DatumPointByMidPoint(
    point1=a.instances['linkage_100-1-lin-2-1'].InterestingPoint(edge=e21[4],
    rule=CENTER), point2=a.instances['linkage_48-2'].InterestingPoint(
    edge=e22[0], rule=CENTER))
a = mdb.models[ModelName].rootAssembly
d11 = a.datums
a.ReferencePoint(point=d11[66])
a = mdb.models[ModelName].rootAssembly
d1 = a.datums
a.ReferencePoint(point=d1[67])
a = mdb.models[ModelName].rootAssembly
d11 = a.datums
a.ReferencePoint(point=d11[68])
a = mdb.models[ModelName].rootAssembly
d1 = a.datums
a.ReferencePoint(point=d1[69])
a = mdb.models[ModelName].rootAssembly
d11 = a.datums
a.ReferencePoint(point=d11[65])
a = mdb.models[ModelName].rootAssembly
d1 = a.datums
a.ReferencePoint(point=d1[64])
a = mdb.models[ModelName].rootAssembly
d11 = a.datums
a.ReferencePoint(point=d11[63])

# RPs-bottom-left
a = mdb.models[ModelName].rootAssembly
e1 = a.instances['linkage_100-2-lin-2-1-1'].edges
e2 = a.instances['box-1'].edges
a.DatumPointByMidPoint(
    point1=a.instances['linkage_100-2-lin-2-1-1'].InterestingPoint(edge=e1[10],
    rule=CENTER), point2=a.instances['box-1'].InterestingPoint(edge=e2[2],
    rule=CENTER))
a = mdb.models[ModelName].rootAssembly
e21 = a.instances['box-1'].edges
e22 = a.instances['linkage_100-2-lin-2-1-1'].edges
a.DatumPointByMidPoint(point1=a.instances['box-1'].InterestingPoint(
    edge=e21[3], rule=CENTER),
    point2=a.instances['linkage_100-2-lin-2-1-1'].InterestingPoint(
    edge=e22[11], rule=CENTER))
a = mdb.models[ModelName].rootAssembly
e1 = a.instances['linkage_100-2'].edges
e2 = a.instances['box-1'].edges
a.DatumPointByMidPoint(point1=a.instances['linkage_100-2'].InterestingPoint(
    edge=e1[11], rule=CENTER), point2=a.instances['box-1'].InterestingPoint(
    edge=e2[3], rule=CENTER))
a = mdb.models[ModelName].rootAssembly
d1 = a.datums
a.ReferencePoint(point=d1[79])
a = mdb.models[ModelName].rootAssembly
d11 = a.datums
a.ReferencePoint(point=d11[78])
a = mdb.models[ModelName].rootAssembly
d1 = a.datums
a.ReferencePoint(point=d1[77])

# RPs-bottom-right
a = mdb.models[ModelName].rootAssembly
e21 = a.instances['linkage_100-2-lin-2-1-lin-2-1'].edges
e22 = a.instances['box-1'].edges
a.DatumPointByMidPoint(
    point1=a.instances['linkage_100-2-lin-2-1-lin-2-1'].InterestingPoint(
    edge=e21[10], rule=CENTER), point2=a.instances['box-1'].InterestingPoint(
    edge=e22[0], rule=CENTER))
a = mdb.models[ModelName].rootAssembly
e1 = a.instances['box-1'].edges
a.DatumPointByMidPoint(point1=a.instances['box-1'].InterestingPoint(edge=e1[0],
    rule=CENTER), point2=a.instances['box-1'].InterestingPoint(edge=e1[1],
    rule=CENTER))
a = mdb.models[ModelName].rootAssembly
e21 = a.instances['box-1'].edges
e22 = a.instances['linkage_100-2-lin-2-1'].edges
a.DatumPointByMidPoint(point1=a.instances['box-1'].InterestingPoint(
    edge=e21[1], rule=CENTER),
    point2=a.instances['linkage_100-2-lin-2-1'].InterestingPoint(edge=e22[11],
    rule=CENTER))
a = mdb.models[ModelName].rootAssembly
d11 = a.datums
a.ReferencePoint(point=d11[85])
a = mdb.models[ModelName].rootAssembly
d1 = a.datums
a.ReferencePoint(point=d1[84])
a = mdb.models[ModelName].rootAssembly
d11 = a.datums
a.ReferencePoint(point=d11[83])
# loule
a = mdb.models[ModelName].rootAssembly
e1 = a.instances['linkage_48-1'].edges
e2 = a.instances['linkage_230-1'].edges
a.DatumPointByMidPoint(point1=a.instances['linkage_48-1'].InterestingPoint(
    edge=e1[1], rule=CENTER),
    point2=a.instances['linkage_230-1'].InterestingPoint(edge=e2[10],
    rule=CENTER))
a = mdb.models[ModelName].rootAssembly
d1 = a.datums
a.ReferencePoint(point=d1[89])

# Couple RPs and faces
# RP1
a = mdb.models[ModelName].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[38], )
region1=a.Set(referencePoints=refPoints1, name='m_Set-1')
a = mdb.models[ModelName].rootAssembly
s1 = a.instances['linkage_100-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#10 ]', ), )
region2=a.Surface(side1Faces=side1Faces1, name='s_Surf-1')
mdb.models[ModelName].Coupling(name='Constraint-1', controlPoint=region1,
    surface=region2, influenceRadius=WHOLE_SURFACE, couplingType=KINEMATIC,
    alpha=0.0, localCsys=None, u1=ON, u2=ON, u3=ON, ur1=ON, ur2=ON, ur3=ON)
# RP2
a = mdb.models[ModelName].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[39], )
region1=a.Set(referencePoints=refPoints1, name='m_Set-2')
a = mdb.models[ModelName].rootAssembly
s1 = a.instances['linkage_100-1-lin-2-1-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#10 ]', ), )
region2=a.Surface(side1Faces=side1Faces1, name='s_Surf-2')
mdb.models[ModelName].Coupling(name='Constraint-2', controlPoint=region1,
    surface=region2, influenceRadius=WHOLE_SURFACE, couplingType=KINEMATIC,
    alpha=0.0, localCsys=None, u1=ON, u2=ON, u3=ON, ur1=ON, ur2=ON, ur3=ON)
# RP3
a = mdb.models[ModelName].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[42], )
region1=a.Set(referencePoints=refPoints1, name='m_Set-3')
a = mdb.models[ModelName].rootAssembly
s1 = a.instances['linkage_100-1-lin-2-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#10 ]', ), )
region2=a.Surface(side1Faces=side1Faces1, name='s_Surf-3')
mdb.models[ModelName].Coupling(name='Constraint-3', controlPoint=region1,
    surface=region2, influenceRadius=WHOLE_SURFACE, couplingType=KINEMATIC,
    alpha=0.0, localCsys=None, u1=ON, u2=ON, u3=ON, ur1=ON, ur2=ON, ur3=ON)
# RP4
a = mdb.models[ModelName].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[43], )
region1=a.Set(referencePoints=refPoints1, name='m_Set-4')
a = mdb.models[ModelName].rootAssembly
s1 = a.instances['linkage_100-1-lin-2-1-lin-2-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#10 ]', ), )
region2=a.Surface(side1Faces=side1Faces1, name='s_Surf-4')
mdb.models[ModelName].Coupling(name='Constraint-4', controlPoint=region1,
    surface=region2, influenceRadius=WHOLE_SURFACE, couplingType=KINEMATIC,
    alpha=0.0, localCsys=None, u1=ON, u2=ON, u3=ON, ur1=ON, ur2=ON, ur3=ON)
# RP5
a = mdb.models[ModelName].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[51], )
region1=a.Set(referencePoints=refPoints1, name='m_Set-5')
a = mdb.models[ModelName].rootAssembly
s1 = a.instances['linkage_100-2'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#20 ]', ), )
region2=a.Surface(side1Faces=side1Faces1, name='s_Surf-5')
mdb.models[ModelName].Coupling(name='Constraint-5', controlPoint=region1,
    surface=region2, influenceRadius=WHOLE_SURFACE, couplingType=KINEMATIC,
    alpha=0.0, localCsys=None, u1=ON, u2=ON, u3=ON, ur1=ON, ur2=ON, ur3=ON)
# RP6
a = mdb.models[ModelName].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[52], )
region1=a.Set(referencePoints=refPoints1, name='m_Set-6')
a = mdb.models[ModelName].rootAssembly
s1 = a.instances['linkage_230-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#20 ]', ), )
region2=a.Surface(side1Faces=side1Faces1, name='s_Surf-6')
mdb.models[ModelName].Coupling(name='Constraint-6', controlPoint=region1,
    surface=region2, influenceRadius=WHOLE_SURFACE, couplingType=KINEMATIC,
    alpha=0.0, localCsys=None, u1=ON, u2=ON, u3=ON, ur1=ON, ur2=ON, ur3=ON)
# RP7
a = mdb.models[ModelName].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[53], )
region1=a.Set(referencePoints=refPoints1, name='m_Set-7')
a = mdb.models[ModelName].rootAssembly
s1 = a.instances['linkage_48-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#1 ]', ), )
region2=a.Surface(side1Faces=side1Faces1, name='s_Surf-7')
mdb.models[ModelName].Coupling(name='Constraint-7', controlPoint=region1,
    surface=region2, influenceRadius=WHOLE_SURFACE, couplingType=KINEMATIC,
    alpha=0.0, localCsys=None, u1=ON, u2=ON, u3=ON, ur1=ON, ur2=ON, ur3=ON)
# RP8
a = mdb.models[ModelName].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[54], )
region1=a.Set(referencePoints=refPoints1, name='m_Set-8')
a = mdb.models[ModelName].rootAssembly
s1 = a.instances['linkage_100-1-lin-2-1-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#20 ]', ), )
region2=a.Surface(side1Faces=side1Faces1, name='s_Surf-8')
mdb.models[ModelName].Coupling(name='Constraint-8', controlPoint=region1,
    surface=region2, influenceRadius=WHOLE_SURFACE, couplingType=KINEMATIC,
    alpha=0.0, localCsys=None, u1=ON, u2=ON, u3=ON, ur1=ON, ur2=ON, ur3=ON)
# RP9
a = mdb.models[ModelName].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[55], )
region1=a.Set(referencePoints=refPoints1, name='m_Set-9')
a = mdb.models[ModelName].rootAssembly
s1 = a.instances['linkage_230-1-lin-2-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#20 ]', ), )
region2=a.Surface(side1Faces=side1Faces1, name='s_Surf-9')
mdb.models[ModelName].Coupling(name='Constraint-9', controlPoint=region1,
    surface=region2, influenceRadius=WHOLE_SURFACE, couplingType=KINEMATIC,
    alpha=0.0, localCsys=None, u1=ON, u2=ON, u3=ON, ur1=ON, ur2=ON, ur3=ON)
# RP10
a = mdb.models[ModelName].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[56], )
region1=a.Set(referencePoints=refPoints1, name='m_Set-10')
a = mdb.models[ModelName].rootAssembly
s1 = a.instances['linkage_100-2-lin-2-1-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#20 ]', ), )
region2=a.Surface(side1Faces=side1Faces1, name='s_Surf-10')
mdb.models[ModelName].Coupling(name='Constraint-10', controlPoint=region1,
    surface=region2, influenceRadius=WHOLE_SURFACE, couplingType=KINEMATIC,
    alpha=0.0, localCsys=None, u1=ON, u2=ON, u3=ON, ur1=ON, ur2=ON, ur3=ON)
# RP11
a = mdb.models[ModelName].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[60], )
region1=a.Set(referencePoints=refPoints1, name='m_Set-11')
a = mdb.models[ModelName].rootAssembly
s1 = a.instances['linkage_230-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#40 ]', ), )
region2=a.Surface(side1Faces=side1Faces1, name='s_Surf-11')
mdb.models[ModelName].Coupling(name='Constraint-11', controlPoint=region1,
    surface=region2, influenceRadius=WHOLE_SURFACE, couplingType=KINEMATIC,
    alpha=0.0, localCsys=None, u1=ON, u2=ON, u3=ON, ur1=ON, ur2=ON, ur3=ON)
# RP12
a = mdb.models[ModelName].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[61], )
region1=a.Set(referencePoints=refPoints1, name='m_Set-12')
a = mdb.models[ModelName].rootAssembly
s1 = a.instances['linkage_64-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#1 ]', ), )
region2=a.Surface(side1Faces=side1Faces1, name='s_Surf-12')
mdb.models[ModelName].Coupling(name='Constraint-12', controlPoint=region1,
    surface=region2, influenceRadius=WHOLE_SURFACE, couplingType=KINEMATIC,
    alpha=0.0, localCsys=None, u1=ON, u2=ON, u3=ON, ur1=ON, ur2=ON, ur3=ON)
# RP13
a = mdb.models[ModelName].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[62], )
region1=a.Set(referencePoints=refPoints1, name='m_Set-13')
a = mdb.models[ModelName].rootAssembly
s1 = a.instances['linkage_230-1-lin-2-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#40 ]', ), )
region2=a.Surface(side1Faces=side1Faces1, name='s_Surf-13')
mdb.models[ModelName].Coupling(name='Constraint-13', controlPoint=region1,
    surface=region2, influenceRadius=WHOLE_SURFACE, couplingType=KINEMATIC,
    alpha=0.0, localCsys=None, u1=ON, u2=ON, u3=ON, ur1=ON, ur2=ON, ur3=ON)
# RP14
a = mdb.models[ModelName].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[70], )
region1=a.Set(referencePoints=refPoints1, name='m_Set-14')
a = mdb.models[ModelName].rootAssembly
s1 = a.instances['linkage_100-2-lin-2-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#20 ]', ), )
region2=a.Surface(side1Faces=side1Faces1, name='s_Surf-14')
mdb.models[ModelName].Coupling(name='Constraint-14', controlPoint=region1,
    surface=region2, influenceRadius=WHOLE_SURFACE, couplingType=KINEMATIC,
    alpha=0.0, localCsys=None, u1=ON, u2=ON, u3=ON, ur1=ON, ur2=ON, ur3=ON)
# RP15
a = mdb.models[ModelName].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[71], )
region1=a.Set(referencePoints=refPoints1, name='m_Set-15')
a = mdb.models[ModelName].rootAssembly
s1 = a.instances['linkage_230-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#10 ]', ), )
region2=a.Surface(side1Faces=side1Faces1, name='s_Surf-15')
mdb.models[ModelName].Coupling(name='Constraint-15', controlPoint=region1, 
    surface=region2, influenceRadius=WHOLE_SURFACE, couplingType=KINEMATIC, 
    alpha=0.0, localCsys=None, u1=ON, u2=ON, u3=ON, ur1=ON, ur2=ON, ur3=ON)
# RP16
a = mdb.models[ModelName].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[72], )
region1=a.Set(referencePoints=refPoints1, name='m_Set-16')
a = mdb.models[ModelName].rootAssembly
s1 = a.instances['linkage_100-1-lin-2-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#20 ]', ), )
region2=a.Surface(side1Faces=side1Faces1, name='s_Surf-16')
mdb.models[ModelName].Coupling(name='Constraint-16', controlPoint=region1,
    surface=region2, influenceRadius=WHOLE_SURFACE, couplingType=KINEMATIC,
    alpha=0.0, localCsys=None, u1=ON, u2=ON, u3=ON, ur1=ON, ur2=ON, ur3=ON)
# RP17
a = mdb.models[ModelName].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[73], )
region1=a.Set(referencePoints=refPoints1, name='m_Set-17')
a = mdb.models[ModelName].rootAssembly
s1 = a.instances['linkage_48-2'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#1 ]', ), )
region2=a.Surface(side1Faces=side1Faces1, name='s_Surf-17')
mdb.models[ModelName].Coupling(name='Constraint-17', controlPoint=region1,
    surface=region2, influenceRadius=WHOLE_SURFACE, couplingType=KINEMATIC,
    alpha=0.0, localCsys=None, u1=ON, u2=ON, u3=ON, ur1=ON, ur2=ON, ur3=ON)
# RP18
a = mdb.models[ModelName].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[74], )
region1=a.Set(referencePoints=refPoints1, name='m_Set-18')
a = mdb.models[ModelName].rootAssembly
s1 = a.instances['linkage_100-1-lin-2-1-lin-2-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#20 ]', ), )
region2=a.Surface(side1Faces=side1Faces1, name='s_Surf-18')
mdb.models[ModelName].Coupling(name='Constraint-18', controlPoint=region1,
    surface=region2, influenceRadius=WHOLE_SURFACE, couplingType=KINEMATIC,
    alpha=0.0, localCsys=None, u1=ON, u2=ON, u3=ON, ur1=ON, ur2=ON, ur3=ON)
# RP19
a = mdb.models[ModelName].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[75], )
region1=a.Set(referencePoints=refPoints1, name='m_Set-19')
a = mdb.models[ModelName].rootAssembly
s1 = a.instances['linkage_230-1-lin-2-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#10 ]', ), )
region2=a.Surface(side1Faces=side1Faces1, name='s_Surf-19')
mdb.models[ModelName].Coupling(name='Constraint-19', controlPoint=region1,
    surface=region2, influenceRadius=WHOLE_SURFACE, couplingType=KINEMATIC,
    alpha=0.0, localCsys=None, u1=ON, u2=ON, u3=ON, ur1=ON, ur2=ON, ur3=ON)
# RP20
a = mdb.models[ModelName].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[76], )
region1=a.Set(referencePoints=refPoints1, name='m_Set-20')
a = mdb.models[ModelName].rootAssembly
s1 = a.instances['linkage_100-2-lin-2-1-lin-2-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#20 ]', ), )
region2=a.Surface(side1Faces=side1Faces1, name='s_Surf-20')
mdb.models[ModelName].Coupling(name='Constraint-20', controlPoint=region1,
    surface=region2, influenceRadius=WHOLE_SURFACE, couplingType=KINEMATIC,
    alpha=0.0, localCsys=None, u1=ON, u2=ON, u3=ON, ur1=ON, ur2=ON, ur3=ON)
# RP21
a = mdb.models[ModelName].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[80], )
region1=a.Set(referencePoints=refPoints1, name='m_Set-21')
a = mdb.models[ModelName].rootAssembly
s1 = a.instances['linkage_100-2'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#10 ]', ), )
region2=a.Surface(side1Faces=side1Faces1, name='s_Surf-21')
mdb.models[ModelName].Coupling(name='Constraint-21', controlPoint=region1,
    surface=region2, influenceRadius=WHOLE_SURFACE, couplingType=KINEMATIC,
    alpha=0.0, localCsys=None, u1=ON, u2=ON, u3=ON, ur1=ON, ur2=ON, ur3=ON)
# RP22
a = mdb.models[ModelName].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[81], )
region1=a.Set(referencePoints=refPoints1, name='m_Set-22')
a = mdb.models[ModelName].rootAssembly
s1 = a.instances['box-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#2 ]', ), )
region2=a.Surface(side1Faces=side1Faces1, name='s_Surf-22')
mdb.models[ModelName].Coupling(name='Constraint-22', controlPoint=region1,
    surface=region2, influenceRadius=WHOLE_SURFACE, couplingType=KINEMATIC,
    alpha=0.0, localCsys=None, u1=ON, u2=ON, u3=ON, ur1=ON, ur2=ON, ur3=ON)
# RP23
a = mdb.models[ModelName].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[82], )
region1=a.Set(referencePoints=refPoints1, name='m_Set-23')
a = mdb.models[ModelName].rootAssembly
s1 = a.instances['linkage_100-2-lin-2-1-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#10 ]', ), )
region2=a.Surface(side1Faces=side1Faces1, name='s_Surf-23')
mdb.models[ModelName].Coupling(name='Constraint-23', controlPoint=region1,
    surface=region2, influenceRadius=WHOLE_SURFACE, couplingType=KINEMATIC,
    alpha=0.0, localCsys=None, u1=ON, u2=ON, u3=ON, ur1=ON, ur2=ON, ur3=ON)
# RP24
a = mdb.models[ModelName].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[86], )
region1=a.Set(referencePoints=refPoints1, name='m_Set-24')
a = mdb.models[ModelName].rootAssembly
s1 = a.instances['linkage_100-2-lin-2-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#10 ]', ), )
region2=a.Surface(side1Faces=side1Faces1, name='s_Surf-24')
mdb.models[ModelName].Coupling(name='Constraint-24', controlPoint=region1,
    surface=region2, influenceRadius=WHOLE_SURFACE, couplingType=KINEMATIC,
    alpha=0.0, localCsys=None, u1=ON, u2=ON, u3=ON, ur1=ON, ur2=ON, ur3=ON)
# RP25
a = mdb.models[ModelName].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[87], )
region1=a.Set(referencePoints=refPoints1, name='m_Set-25')
a = mdb.models[ModelName].rootAssembly
s1 = a.instances['box-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#1 ]', ), )
region2=a.Surface(side1Faces=side1Faces1, name='s_Surf-25')
mdb.models[ModelName].Coupling(name='Constraint-25', controlPoint=region1,
    surface=region2, influenceRadius=WHOLE_SURFACE, couplingType=KINEMATIC,
    alpha=0.0, localCsys=None, u1=ON, u2=ON, u3=ON, ur1=ON, ur2=ON, ur3=ON)
# RP26
a = mdb.models[ModelName].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[88], )
region1=a.Set(referencePoints=refPoints1, name='m_Set-26')
a = mdb.models[ModelName].rootAssembly
s1 = a.instances['linkage_100-2-lin-2-1-lin-2-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#10 ]', ), )
region2=a.Surface(side1Faces=side1Faces1, name='s_Surf-26')
mdb.models[ModelName].Coupling(name='Constraint-26', controlPoint=region1,
    surface=region2, influenceRadius=WHOLE_SURFACE, couplingType=KINEMATIC,
    alpha=0.0, localCsys=None, u1=ON, u2=ON, u3=ON, ur1=ON, ur2=ON, ur3=ON)
# RP27
a = mdb.models[ModelName].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[90], )
region1=a.Set(referencePoints=refPoints1, name='m_Set-27')
a = mdb.models[ModelName].rootAssembly
s1 = a.instances['linkage_100-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#20 ]', ), )
region2=a.Surface(side1Faces=side1Faces1, name='s_Surf-27')
mdb.models[ModelName].Coupling(name='Constraint-27', controlPoint=region1,
    surface=region2, influenceRadius=WHOLE_SURFACE, couplingType=KINEMATIC,
    alpha=0.0, localCsys=None, u1=ON, u2=ON, u3=ON, ur1=ON, ur2=ON, ur3=ON)


# Interaction-hinge

# Create connect property
mdb.models[ModelName].ConnectorSection(name='ConnSect-1', assembledType=HINGE)

# RP1 to ground
r1 = a.referencePoints
dtm1 = a.DatumCsysByThreePoints(origin=r1[38], coordSysType=CARTESIAN, line1=(
    1.0, 0.0, 0.0), line2=(0.0, 1.0, 0.0))
dtmid1 = a.datums[dtm1.id]
a = mdb.models[ModelName].rootAssembly
r11 = a.referencePoints
wire = a.WirePolyLine(points=((r11[38], None), ), mergeType=IMPRINT,
    meshable=False)
oldName = wire.name
mdb.models[ModelName].rootAssembly.features.changeKey(fromName=oldName,
    toName='Wire-1')
a = mdb.models[ModelName].rootAssembly
e1 = a.edges
edges1 = e1.getSequenceFromMask(mask=('[#1 ]', ), )
a.Set(edges=edges1, name='Wire-1-Set-1')
region = mdb.models[ModelName].rootAssembly.sets['Wire-1-Set-1']
csa = a.SectionAssignment(sectionName='ConnSect-1', region=region)
#: The section "ConnSect-1" has been assigned to 1 wire or attachment line.
a.ConnectorOrientation(region=csa.getSet(), localCsys1=dtmid1)

# RP2 to ground
dtm1 = a.DatumCsysByThreePoints(origin=r11[39], coordSysType=CARTESIAN, line1=(
    1.0, 0.0, 0.0), line2=(0.0, 1.0, 0.0))
dtmid1 = a.datums[dtm1.id]
a = mdb.models[ModelName].rootAssembly
r1 = a.referencePoints
wire = a.WirePolyLine(points=((r1[39], None), ), mergeType=IMPRINT,
    meshable=False)
oldName = wire.name
mdb.models[ModelName].rootAssembly.features.changeKey(fromName=oldName,
    toName='Wire-2')
a = mdb.models[ModelName].rootAssembly
e1 = a.edges
edges1 = e1.getSequenceFromMask(mask=('[#1 ]', ), )
a.Set(edges=edges1, name='Wire-2-Set-1')
region = mdb.models[ModelName].rootAssembly.sets['Wire-2-Set-1']
csa = a.SectionAssignment(sectionName='ConnSect-1', region=region)
#: The section "ConnSect-1" has been assigned to 1 wire or attachment line.
a.ConnectorOrientation(region=csa.getSet(), localCsys1=dtmid1)

# RP3 to ground
dtm1 = a.DatumCsysByThreePoints(origin=r1[42], coordSysType=CARTESIAN, line1=(
    1.0, 0.0, 0.0), line2=(0.0, 1.0, 0.0))
dtmid1 = a.datums[dtm1.id]
a = mdb.models[ModelName].rootAssembly
r11 = a.referencePoints
wire = a.WirePolyLine(points=((r11[42], None), ), mergeType=IMPRINT,
    meshable=False)
oldName = wire.name
mdb.models[ModelName].rootAssembly.features.changeKey(fromName=oldName,
    toName='Wire-3')
a = mdb.models[ModelName].rootAssembly
e1 = a.edges
edges1 = e1.getSequenceFromMask(mask=('[#1 ]', ), )
a.Set(edges=edges1, name='Wire-3-Set-1')
region = mdb.models[ModelName].rootAssembly.sets['Wire-3-Set-1']
csa = a.SectionAssignment(sectionName='ConnSect-1', region=region)
#: The section "ConnSect-1" has been assigned to 1 wire or attachment line.
a.ConnectorOrientation(region=csa.getSet(), localCsys1=dtmid1)

# RP4 to ground
dtm1 = a.DatumCsysByThreePoints(origin=r11[43], coordSysType=CARTESIAN, line1=(
    1.0, 0.0, 0.0), line2=(0.0, 1.0, 0.0))
dtmid1 = a.datums[dtm1.id]
a = mdb.models[ModelName].rootAssembly
r1 = a.referencePoints
wire = a.WirePolyLine(points=((r1[43], None), ), mergeType=IMPRINT,
    meshable=False)
oldName = wire.name
mdb.models[ModelName].rootAssembly.features.changeKey(fromName=oldName,
    toName='Wire-4')
a = mdb.models[ModelName].rootAssembly
e1 = a.edges
edges1 = e1.getSequenceFromMask(mask=('[#1 ]', ), )
a.Set(edges=edges1, name='Wire-4-Set-1')
region = mdb.models[ModelName].rootAssembly.sets['Wire-4-Set-1']
csa = a.SectionAssignment(sectionName='ConnSect-1', region=region)
#: The section "ConnSect-1" has been assigned to 1 wire or attachment line.
a.ConnectorOrientation(region=csa.getSet(), localCsys1=dtmid1)

# RP5-RP6
dtm1 = a.DatumCsysByThreePoints(origin=r1[51], coordSysType=CARTESIAN, line1=(
    1.0, 0.0, 0.0), line2=(0.0, 1.0, 0.0))
dtmid1 = a.datums[dtm1.id]
a = mdb.models[ModelName].rootAssembly
r11 = a.referencePoints
wire = a.WirePolyLine(points=((r11[51], r11[52]), ), mergeType=IMPRINT,
    meshable=False)
oldName = wire.name
mdb.models[ModelName].rootAssembly.features.changeKey(fromName=oldName,
    toName='Wire-5')
a = mdb.models[ModelName].rootAssembly
e1 = a.edges
edges1 = e1.getSequenceFromMask(mask=('[#1 ]', ), )
a.Set(edges=edges1, name='Wire-5-Set-1')
region = mdb.models[ModelName].rootAssembly.sets['Wire-5-Set-1']
csa = a.SectionAssignment(sectionName='ConnSect-1', region=region)
#: The section "ConnSect-1" has been assigned to 1 wire or attachment line.
a.ConnectorOrientation(region=csa.getSet(), localCsys1=dtmid1)

# RP6-RP27
dtm1 = a.DatumCsysByThreePoints(origin=r11[52], coordSysType=CARTESIAN, line1=(
    1.0, 0.0, 0.0), line2=(0.0, 1.0, 0.0))
dtmid1 = a.datums[dtm1.id]
a = mdb.models[ModelName].rootAssembly
r1 = a.referencePoints
wire = a.WirePolyLine(points=((r1[52], r1[90]), ), mergeType=IMPRINT,
    meshable=False)
oldName = wire.name
mdb.models[ModelName].rootAssembly.features.changeKey(fromName=oldName,
    toName='Wire-6')
a = mdb.models[ModelName].rootAssembly
e1 = a.edges
edges1 = e1.getSequenceFromMask(mask=('[#1 ]', ), )
a.Set(edges=edges1, name='Wire-6-Set-1')
region = mdb.models[ModelName].rootAssembly.sets['Wire-6-Set-1']
csa = a.SectionAssignment(sectionName='ConnSect-1', region=region)
#: The section "ConnSect-1" has been assigned to 1 wire or attachment line.
a.ConnectorOrientation(region=csa.getSet(), localCsys1=dtmid1)

# RP27-RP7
dtm1 = a.DatumCsysByThreePoints(origin=r1[90], coordSysType=CARTESIAN, line1=(
    1.0, 0.0, 0.0), line2=(0.0, 1.0, 0.0))
dtmid1 = a.datums[dtm1.id]
a = mdb.models[ModelName].rootAssembly
r11 = a.referencePoints
wire = a.WirePolyLine(points=((r11[90], r11[53]), ), mergeType=IMPRINT,
    meshable=False)
oldName = wire.name
mdb.models[ModelName].rootAssembly.features.changeKey(fromName=oldName,
    toName='Wire-7')
a = mdb.models[ModelName].rootAssembly
e1 = a.edges
edges1 = e1.getSequenceFromMask(mask=('[#1 ]', ), )
a.Set(edges=edges1, name='Wire-7-Set-1')
region = mdb.models[ModelName].rootAssembly.sets['Wire-7-Set-1']
csa = a.SectionAssignment(sectionName='ConnSect-1', region=region)
#: The section "ConnSect-1" has been assigned to 1 wire or attachment line.
a.ConnectorOrientation(region=csa.getSet(), localCsys1=dtmid1)

# RP7-RP8
dtm1 = a.DatumCsysByThreePoints(origin=r11[54], coordSysType=CARTESIAN, line1=(
    1.0, 0.0, 0.0), line2=(0.0, 1.0, 0.0))
dtmid1 = a.datums[dtm1.id]
a = mdb.models[ModelName].rootAssembly
r1 = a.referencePoints
wire = a.WirePolyLine(points=((r1[54], r1[53]), ), mergeType=IMPRINT,
    meshable=False)
oldName = wire.name
mdb.models[ModelName].rootAssembly.features.changeKey(fromName=oldName,
    toName='Wire-8')
a = mdb.models[ModelName].rootAssembly
e1 = a.edges
edges1 = e1.getSequenceFromMask(mask=('[#1 ]', ), )
a.Set(edges=edges1, name='Wire-8-Set-1')
region = mdb.models[ModelName].rootAssembly.sets['Wire-8-Set-1']
csa = a.SectionAssignment(sectionName='ConnSect-1', region=region)
#: The section "ConnSect-1" has been assigned to 1 wire or attachment line.
a.ConnectorOrientation(region=csa.getSet(), localCsys1=dtmid1)

# RP8-RP9
dtm1 = a.DatumCsysByThreePoints(origin=r1[55], coordSysType=CARTESIAN, line1=(
    1.0, 0.0, 0.0), line2=(0.0, 1.0, 0.0))
dtmid1 = a.datums[dtm1.id]
a = mdb.models[ModelName].rootAssembly
r11 = a.referencePoints
wire = a.WirePolyLine(points=((r11[55], r11[54]), ), mergeType=IMPRINT,
    meshable=False)
oldName = wire.name
mdb.models[ModelName].rootAssembly.features.changeKey(fromName=oldName,
    toName='Wire-9')
a = mdb.models[ModelName].rootAssembly
e1 = a.edges
edges1 = e1.getSequenceFromMask(mask=('[#1 ]', ), )
a.Set(edges=edges1, name='Wire-9-Set-1')
region = mdb.models[ModelName].rootAssembly.sets['Wire-9-Set-1']
csa = a.SectionAssignment(sectionName='ConnSect-1', region=region)
#: The section "ConnSect-1" has been assigned to 1 wire or attachment line.
a.ConnectorOrientation(region=csa.getSet(), localCsys1=dtmid1)

# RP9-RP10
dtm1 = a.DatumCsysByThreePoints(origin=r11[56], coordSysType=CARTESIAN, line1=(
    1.0, 0.0, 0.0), line2=(0.0, 1.0, 0.0))
dtmid1 = a.datums[dtm1.id]
a = mdb.models[ModelName].rootAssembly
r1 = a.referencePoints
wire = a.WirePolyLine(points=((r1[56], r1[55]), ), mergeType=IMPRINT,
    meshable=False)
oldName = wire.name
mdb.models[ModelName].rootAssembly.features.changeKey(fromName=oldName,
    toName='Wire-10')
a = mdb.models[ModelName].rootAssembly
e1 = a.edges
edges1 = e1.getSequenceFromMask(mask=('[#1 ]', ), )
a.Set(edges=edges1, name='Wire-10-Set-1')
region = mdb.models[ModelName].rootAssembly.sets['Wire-10-Set-1']
csa = a.SectionAssignment(sectionName='ConnSect-1', region=region)
#: The section "ConnSect-1" has been assigned to 1 wire or attachment line.
a.ConnectorOrientation(region=csa.getSet(), localCsys1=dtmid1)

# RP11-RP12
dtm1 = a.DatumCsysByThreePoints(origin=r1[60], point1=r1[61],
    coordSysType=CARTESIAN)
dtmid1 = a.datums[dtm1.id]
a = mdb.models[ModelName].rootAssembly
r11 = a.referencePoints
wire = a.WirePolyLine(points=((r11[60], r11[61]), ), mergeType=IMPRINT,
    meshable=False)
oldName = wire.name
mdb.models[ModelName].rootAssembly.features.changeKey(fromName=oldName,
    toName='Wire-11')
a = mdb.models[ModelName].rootAssembly
e1 = a.edges
edges1 = e1.getSequenceFromMask(mask=('[#1 ]', ), )
a.Set(edges=edges1, name='Wire-11-Set-1')
region = mdb.models[ModelName].rootAssembly.sets['Wire-11-Set-1']
csa = a.SectionAssignment(sectionName='ConnSect-1', region=region)
#: The section "ConnSect-1" has been assigned to 1 wire or attachment line.
a.ConnectorOrientation(region=csa.getSet(), localCsys1=dtmid1)

# RP12-RP13
dtm1 = a.DatumCsysByThreePoints(origin=r11[62], point1=r11[61],
    coordSysType=CARTESIAN)
dtmid1 = a.datums[dtm1.id]
a = mdb.models[ModelName].rootAssembly
r1 = a.referencePoints
wire = a.WirePolyLine(points=((r1[62], r1[61]), ), mergeType=IMPRINT,
    meshable=False)
oldName = wire.name
mdb.models[ModelName].rootAssembly.features.changeKey(fromName=oldName,
    toName='Wire-12')
a = mdb.models[ModelName].rootAssembly
e1 = a.edges
edges1 = e1.getSequenceFromMask(mask=('[#1 ]', ), )
a.Set(edges=edges1, name='Wire-12-Set-1')
region = mdb.models[ModelName].rootAssembly.sets['Wire-12-Set-1']
csa = a.SectionAssignment(sectionName='ConnSect-1', region=region)
#: The section "ConnSect-1" has been assigned to 1 wire or attachment line.
a.ConnectorOrientation(region=csa.getSet(), localCsys1=dtmid1)

# RP14-RP15
dtm1 = a.DatumCsysByThreePoints(origin=r1[70], point1=r1[71],
    coordSysType=CARTESIAN)
dtmid1 = a.datums[dtm1.id]
a = mdb.models[ModelName].rootAssembly
r11 = a.referencePoints
wire = a.WirePolyLine(points=((r11[70], r11[71]), ), mergeType=IMPRINT,
    meshable=False)
oldName = wire.name
mdb.models[ModelName].rootAssembly.features.changeKey(fromName=oldName,
    toName='Wire-13')
a = mdb.models[ModelName].rootAssembly
e1 = a.edges
edges1 = e1.getSequenceFromMask(mask=('[#1 ]', ), )
a.Set(edges=edges1, name='Wire-13-Set-1')
region = mdb.models[ModelName].rootAssembly.sets['Wire-13-Set-1']
csa = a.SectionAssignment(sectionName='ConnSect-1', region=region)
#: The section "ConnSect-1" has been assigned to 1 wire or attachment line.
a.ConnectorOrientation(region=csa.getSet(), localCsys1=dtmid1)

# RP15-RP16
dtm1 = a.DatumCsysByThreePoints(origin=r11[71], point1=r11[72],
    coordSysType=CARTESIAN)
dtmid1 = a.datums[dtm1.id]
a = mdb.models[ModelName].rootAssembly
r1 = a.referencePoints
wire = a.WirePolyLine(points=((r1[71], r1[72]), ), mergeType=IMPRINT,
    meshable=False)
oldName = wire.name
mdb.models[ModelName].rootAssembly.features.changeKey(fromName=oldName,
    toName='Wire-14')
a = mdb.models[ModelName].rootAssembly
e1 = a.edges
edges1 = e1.getSequenceFromMask(mask=('[#1 ]', ), )
a.Set(edges=edges1, name='Wire-14-Set-1')
region = mdb.models[ModelName].rootAssembly.sets['Wire-14-Set-1']
csa = a.SectionAssignment(sectionName='ConnSect-1', region=region)
#: The section "ConnSect-1" has been assigned to 1 wire or attachment line.
a.ConnectorOrientation(region=csa.getSet(), localCsys1=dtmid1)

# RP16-RP17
dtm1 = a.DatumCsysByThreePoints(origin=r1[72], point1=r1[73],
    coordSysType=CARTESIAN)
dtmid1 = a.datums[dtm1.id]
a = mdb.models[ModelName].rootAssembly
r11 = a.referencePoints
wire = a.WirePolyLine(points=((r11[72], r11[73]), ), mergeType=IMPRINT,
    meshable=False)
oldName = wire.name
mdb.models[ModelName].rootAssembly.features.changeKey(fromName=oldName,
    toName='Wire-15')
a = mdb.models[ModelName].rootAssembly
e1 = a.edges
edges1 = e1.getSequenceFromMask(mask=('[#1 ]', ), )
a.Set(edges=edges1, name='Wire-15-Set-1')
region = mdb.models[ModelName].rootAssembly.sets['Wire-15-Set-1']
csa = a.SectionAssignment(sectionName='ConnSect-1', region=region)
#: The section "ConnSect-1" has been assigned to 1 wire or attachment line.
a.ConnectorOrientation(region=csa.getSet(), localCsys1=dtmid1)

# RP17-RP18
dtm1 = a.DatumCsysByThreePoints(origin=r11[74], point1=r11[73],
    coordSysType=CARTESIAN)
dtmid1 = a.datums[dtm1.id]
a = mdb.models[ModelName].rootAssembly
r1 = a.referencePoints
wire = a.WirePolyLine(points=((r1[74], r1[73]), ), mergeType=IMPRINT,
    meshable=False)
oldName = wire.name
mdb.models[ModelName].rootAssembly.features.changeKey(fromName=oldName,
    toName='Wire-16')
a = mdb.models[ModelName].rootAssembly
e1 = a.edges
edges1 = e1.getSequenceFromMask(mask=('[#1 ]', ), )
a.Set(edges=edges1, name='Wire-16-Set-1')
region = mdb.models[ModelName].rootAssembly.sets['Wire-16-Set-1']
csa = a.SectionAssignment(sectionName='ConnSect-1', region=region)
#: The section "ConnSect-1" has been assigned to 1 wire or attachment line.
a.ConnectorOrientation(region=csa.getSet(), localCsys1=dtmid1)

# RP18-RP19
dtm1 = a.DatumCsysByThreePoints(origin=r1[75], point1=r1[74],
    coordSysType=CARTESIAN)
dtmid1 = a.datums[dtm1.id]
a = mdb.models[ModelName].rootAssembly
r11 = a.referencePoints
wire = a.WirePolyLine(points=((r11[75], r11[74]), ), mergeType=IMPRINT,
    meshable=False)
oldName = wire.name
mdb.models[ModelName].rootAssembly.features.changeKey(fromName=oldName,
    toName='Wire-17')
a = mdb.models[ModelName].rootAssembly
e1 = a.edges
edges1 = e1.getSequenceFromMask(mask=('[#1 ]', ), )
a.Set(edges=edges1, name='Wire-17-Set-1')
region = mdb.models[ModelName].rootAssembly.sets['Wire-17-Set-1']
csa = a.SectionAssignment(sectionName='ConnSect-1', region=region)
#: The section "ConnSect-1" has been assigned to 1 wire or attachment line.
a.ConnectorOrientation(region=csa.getSet(), localCsys1=dtmid1)

# RP19-RP20
dtm1 = a.DatumCsysByThreePoints(origin=r11[76], point1=r11[75],
    coordSysType=CARTESIAN)
dtmid1 = a.datums[dtm1.id]
a = mdb.models[ModelName].rootAssembly
r1 = a.referencePoints
wire = a.WirePolyLine(points=((r1[76], r1[75]), ), mergeType=IMPRINT,
    meshable=False)
oldName = wire.name
mdb.models[ModelName].rootAssembly.features.changeKey(fromName=oldName,
    toName='Wire-18')
a = mdb.models[ModelName].rootAssembly
e1 = a.edges
edges1 = e1.getSequenceFromMask(mask=('[#1 ]', ), )
a.Set(edges=edges1, name='Wire-18-Set-1')
region = mdb.models[ModelName].rootAssembly.sets['Wire-18-Set-1']
csa = a.SectionAssignment(sectionName='ConnSect-1', region=region)
#: The section "ConnSect-1" has been assigned to 1 wire or attachment line.
a.ConnectorOrientation(region=csa.getSet(), localCsys1=dtmid1)

# RP21-RP22
dtm1 = a.DatumCsysByThreePoints(origin=r1[80], point1=r1[81],
    coordSysType=CARTESIAN)
dtmid1 = a.datums[dtm1.id]
a = mdb.models[ModelName].rootAssembly
r11 = a.referencePoints
wire = a.WirePolyLine(points=((r11[80], r11[81]), ), mergeType=IMPRINT,
    meshable=False)
oldName = wire.name
mdb.models[ModelName].rootAssembly.features.changeKey(fromName=oldName,
    toName='Wire-19')
a = mdb.models[ModelName].rootAssembly
e1 = a.edges
edges1 = e1.getSequenceFromMask(mask=('[#1 ]', ), )
a.Set(edges=edges1, name='Wire-19-Set-1')
region = mdb.models[ModelName].rootAssembly.sets['Wire-19-Set-1']
csa = a.SectionAssignment(sectionName='ConnSect-1', region=region)
#: The section "ConnSect-1" has been assigned to 1 wire or attachment line.
a.ConnectorOrientation(region=csa.getSet(), localCsys1=dtmid1)

# RP22-RP23
dtm1 = a.DatumCsysByThreePoints(origin=r11[82], point1=r11[81],
    coordSysType=CARTESIAN)
dtmid1 = a.datums[dtm1.id]
a = mdb.models[ModelName].rootAssembly
r1 = a.referencePoints
wire = a.WirePolyLine(points=((r1[82], r1[81]), ), mergeType=IMPRINT,
    meshable=False)
oldName = wire.name
mdb.models[ModelName].rootAssembly.features.changeKey(fromName=oldName,
    toName='Wire-20')
a = mdb.models[ModelName].rootAssembly
e1 = a.edges
edges1 = e1.getSequenceFromMask(mask=('[#1 ]', ), )
a.Set(edges=edges1, name='Wire-20-Set-1')
region = mdb.models[ModelName].rootAssembly.sets['Wire-20-Set-1']
csa = a.SectionAssignment(sectionName='ConnSect-1', region=region)
#: The section "ConnSect-1" has been assigned to 1 wire or attachment line.
a.ConnectorOrientation(region=csa.getSet(), localCsys1=dtmid1)

# RP24-RP25
dtm1 = a.DatumCsysByThreePoints(origin=r1[86], point1=r1[87],
    coordSysType=CARTESIAN)
dtmid1 = a.datums[dtm1.id]
a = mdb.models[ModelName].rootAssembly
r11 = a.referencePoints
wire = a.WirePolyLine(points=((r11[86], r11[87]), ), mergeType=IMPRINT,
    meshable=False)
oldName = wire.name
mdb.models[ModelName].rootAssembly.features.changeKey(fromName=oldName,
    toName='Wire-21')
a = mdb.models[ModelName].rootAssembly
e1 = a.edges
edges1 = e1.getSequenceFromMask(mask=('[#1 ]', ), )
a.Set(edges=edges1, name='Wire-21-Set-1')
region = mdb.models[ModelName].rootAssembly.sets['Wire-21-Set-1']
csa = a.SectionAssignment(sectionName='ConnSect-1', region=region)
#: The section "ConnSect-1" has been assigned to 1 wire or attachment line.
a.ConnectorOrientation(region=csa.getSet(), localCsys1=dtmid1)

# RP25-RP26
dtm1 = a.DatumCsysByThreePoints(origin=r11[88], point1=r11[87],
    coordSysType=CARTESIAN)
dtmid1 = a.datums[dtm1.id]
a = mdb.models[ModelName].rootAssembly
r1 = a.referencePoints
wire = a.WirePolyLine(points=((r1[88], r1[87]), ), mergeType=IMPRINT,
    meshable=False)
oldName = wire.name
mdb.models[ModelName].rootAssembly.features.changeKey(fromName=oldName,
    toName='Wire-22')
a = mdb.models[ModelName].rootAssembly
e1 = a.edges
edges1 = e1.getSequenceFromMask(mask=('[#1 ]', ), )
a.Set(edges=edges1, name='Wire-22-Set-1')
region = mdb.models[ModelName].rootAssembly.sets['Wire-22-Set-1']
csa = a.SectionAssignment(sectionName='ConnSect-1', region=region)
#: The section "ConnSect-1" has been assigned to 1 wire or attachment line.
a.ConnectorOrientation(region=csa.getSet(), localCsys1=dtmid1)

# Tie
a = mdb.models[ModelName].rootAssembly
s1 = a.instances['shell-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#2 ]', ), )
region1=a.Surface(side1Faces=side1Faces1, name='m_Surf-28')
a = mdb.models[ModelName].rootAssembly
s1 = a.instances['box-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#30 ]', ), )
region2=a.Surface(side1Faces=side1Faces1, name='s_Surf-28')
mdb.models[ModelName].Tie(name='Constraint-28', main=region1,
    secondary=region2, positionToleranceMethod=COMPUTED, adjust=ON,
    tieRotations=ON, thickness=ON)

# General contact
mdb.models[ModelName].ContactProperty(
    'IntProp-1')
mdb.models[ModelName].interactionProperties['IntProp-1'].TangentialBehavior(
    formulation=FRICTIONLESS)
mdb.models[ModelName].interactionProperties['IntProp-1'].NormalBehavior(
    pressureOverclosure=HARD, allowSeparation=ON, 
    constraintEnforcementMethod=DEFAULT)
#: The interaction property "IntProp-1" has been created.
mdb.models[ModelName].ContactStd(
    name='Int-1', createStepName='Initial')
mdb.models[ModelName].interactions['Int-1'].includedPairs.setValuesInStep(
    stepName='Initial', useAllstar=ON)
mdb.models[ModelName].interactions['Int-1'].contactPropertyAssignments.appendInStep(
    stepName='Initial', assignments=((GLOBAL, SELF, 'IntProp-1'), ))
#: The interaction "Int-1" has been created.


# Step
# Linear perturbation-Frequency AMS
mdb.models[ModelName].FrequencyStep(name='Step-1', previous='Initial',
    maxEigen=10000.0, simLinearDynamics=ON, normalization=MASS, minEigen=1.0,
    eigensolver=AMS, numEigen=10, acousticCoupling=AC_PROJECTION)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')


# Load-boundary

# 4 RPs
a = mdb.models[ModelName].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[38], r1[39], r1[42], r1[43], )
region = a.Set(referencePoints=refPoints1, name='Set-50')
mdb.models[ModelName].DisplacementBC(name='BC-1', createStepName='Initial',
    region=region, u1=SET, u2=SET, u3=SET, ur1=UNSET, ur2=UNSET, ur3=UNSET,
    amplitude=UNSET, distributionType=UNIFORM, fieldName='', localCsys=None)

# Assumption: shell is pushed on the ring firmly
a = mdb.models[ModelName].rootAssembly
c1 = a.instances['shell-1'].cells
cells1 = c1.getSequenceFromMask(mask=('[#1 ]', ), )
f1 = a.instances['shell-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#f ]', ), )
e1 = a.instances['shell-1'].edges
edges1 = e1.getSequenceFromMask(mask=('[#f ]', ), )
region = a.Set(edges=edges1, faces=faces1, cells=cells1,
    name='Set-51')
mdb.models[ModelName].DisplacementBC(name='BC-2', createStepName='Initial',
    region=region, u1=UNSET, u2=UNSET, u3=UNSET, ur1=SET, ur2=UNSET, ur3=SET,
    amplitude=UNSET, distributionType=UNIFORM, fieldName='', localCsys=None)


# Mesh

# Box
p = mdb.models[ModelName].parts['box']
p.seedPart(size=8.0, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models[ModelName].parts['box']
e = p.edges
pickedEdges = e.getSequenceFromMask(mask=('[#a ]', ), )
p.seedEdgeByNumber(edges=pickedEdges, number=12, constraint=FINER)
p = mdb.models[ModelName].parts['box']
p.generateMesh()

# Linkage_48
p = mdb.models[ModelName].parts['linkage_48']
p.seedPart(size=3.0, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models[ModelName].parts['linkage_48']
p.generateMesh()

# Linkage_64
p = mdb.models[ModelName].parts['linkage_64']
p.seedPart(size=3.0, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models[ModelName].parts['linkage_64']
p.generateMesh()

# Linkage_100
p = mdb.models[ModelName].parts['linkage_100']
p.seedPart(size=3.0, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models[ModelName].parts['linkage_100']
p.generateMesh()

# Linkage_230
p = mdb.models[ModelName].parts['linkage_230']
p.seedPart(size=2.0, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models[ModelName].parts['linkage_230']
p.generateMesh()

# Shell
p = mdb.models[ModelName].parts['shell']
c = p.cells
pickedCells = c.getSequenceFromMask(mask=('[#1 ]', ), )
v1, e2, d3 = p.vertices, p.edges, p.datums
p.PartitionCellByPlaneThreePoints(cells=pickedCells, point1=p.InterestingPoint(
    edge=e2[0], rule=CENTER), point2=p.InterestingPoint(edge=e2[1],
    rule=CENTER), point3=p.InterestingPoint(edge=e2[2], rule=MIDDLE))
p = mdb.models[ModelName].parts['shell']
p.seedPart(size=10.0, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models[ModelName].parts['shell']
e = p.edges
pickedEdges = e.getSequenceFromMask(mask=('[#28 ]', ), )
p.seedEdgeByNumber(edges=pickedEdges, number=3, constraint=FINER)
p = mdb.models[ModelName].parts['shell']
p.generateMesh()


# Job
Name=ModelName
Name=Name.replace(' ','-')
mdb.Job(name=Name, model=ModelName, description='', type=ANALYSIS,
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90,
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True,
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF,
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='',
    scratch='', resultsFormat=ODB, numThreadsPerMpiProcess=1,
    multiprocessingMode=DEFAULT, numCpus=4, numDomains=4, numGPUs=0)

mdb.jobs[Name].writeInput(consistencyChecking=OFF)
#: The job input file has been written to "Job-1.inp".
#mdb.jobs['Job-1'].submit(consistencyChecking=OFF)