import mavspy.mavs as mavs

#------------------ scene ----------------------------------------------#
scene = mavs.MavsEmbreeScene()
mavs_scenefile = "/scenes/cube_scene.json"
scene.Load(mavs.mavs_data_path+mavs_scenefile)

#------------------ environment ----------------------------------------#
env = mavs.MavsEnvironment()
env.SetScene(scene)
env.SetFog(20.0) # 0-100
#------------------ vehicle --------------------------------------------#
veh = mavs.MavsRp3d()
veh_file = 'mrzr4_tires_low_gear.json'
veh.Load(mavs.mavs_data_path+'/vehicles/rp3d_vehicles/' + veh_file)
veh.SetInitialPosition(50.0, 0.0, 2.0) # in global ENU
veh.SetInitialHeading(3.14159) # in radians

#------------------ camera ---------------------------------------------#
 # window must be highlighted to input driving commands
drive_cam = mavs.MavsCamera()
 # nx,ny,dx,dy,focal_len
drive_cam.Initialize(786,512,0.005373,0.0035,0.0035)
# Set camera compression and gain
drive_cam.SetGammaAndGain(0.75,1.0) 
# offset of camera from vehicle CG
drive_cam.SetOffset([-10.0,0.0,3.0],[1.0,0.0,0.0,0.0]) 
# Turn on/off shadows for this camera 
drive_cam.RenderShadows(True) 
# do the initial camera update and display
drive_cam.Update(env, 0.1)
drive_cam.Display()

#------------------ lidar ----------------------------------------------#
lidar = mavs.MavsLidar('OS1')
lidar.SetOffset([0.0, 0.0, 2.0],[1.0, 0.0, 0.0, 0.0])

#------------------ main loop ------------------------------------------#
dt = 1.0/100.0 # time step, seconds
n = 0 # loop counter
while (drive_cam.DisplayOpen()):
    # Get the driving command
    dc = drive_cam.GetDrivingCommand() 
    # Update the vehicle with the driving command
    veh.Update(env, dc.throttle, dc.steering, dc.braking, dt) 
    
    # get the current position and orientation of the vehicle
    position = veh.GetPosition()
    orientation = veh.GetOrientation()
    
    # update the sensors
    if (n%10==0):
        lidar.SetPose(position,orientation)
        lidar.Update(env,0.05)
        lidar.Display()
    if n%6==0:
        drive_cam.SetPose(position,orientation)
        drive_cam.Update(env,0.05)
        drive_cam.Display()
    n = n+1