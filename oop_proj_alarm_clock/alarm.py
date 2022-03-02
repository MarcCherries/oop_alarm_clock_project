class AlarmClock:
    def __init__ (self):
        self.current_time = '1100'
        self.is_alarm_set =  True
        self.alarm_time_to_sound = '1400'
    
    def set_current_time (self):
        self.current_time = input('Please enter the current time (0001 - 2400) \n')
        print(f'The new current time is {self.current_time}')

    def toggle_alarm_on_off (self):
        self.is_alarm_set = str.upper(input ('Press Y to toggle on, N to toggle off \n'))
        if self.is_alarm_set == 'Y':
           self.is_alarm_set = True
           print(f'Alarm is currently set for {self.alarm_time_to_sound}!')
        else:
            self.is_alarm_set = False
            print('Alarm is not set!')



    def set_alarm_time_to_sound (self):
        self.alarm_time_to_sound = input('Please enter the time for your alarm to sound (0001 - 2400 \n')
        print(f'The alarm is set for {self.alarm_time_to_sound}')
        
        
           
