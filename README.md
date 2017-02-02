In order for the safety controller to funtion properly, please add the following lines in your twist_mux config file:

- name    : safety_controller
  topic   : safety_controller/cmd_vel
  timeout : 1.5
  priority: 100
