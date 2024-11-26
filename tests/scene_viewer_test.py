import mavspy.mavs as mavs

scene = mavs.MavsEmbreeScene()
mavs_scenefile = "/scenes/cube_scene.json"
scene.Load(mavs.mavs_data_path+mavs_scenefile)

env = mavs.MavsEnvironment()
env.SetScene(scene)

cam = mavs.MavsCamera()
cam.Initialize(786,512,0.005373,0.0035,0.0035)
cam.SetGammaAndGain(0.75,1.0)
cam.SetPose([0, 0,2], [1.0, 0.0, 0.0, 0.0])
cam.FreePose()

# do the first camera update
dt = 1.0/30.0
position, orientation = cam.GetPose()
cam.SetPose(position,orientation)
cam.Update(env,dt)
cam.Display()

while (cam.DisplayOpen()):
    position, orientation = cam.GetPose()
    cam.SetPose(position,orientation)
    cam.Update(env,dt)
    cam.Display()