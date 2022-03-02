from alarm import AlarmClock

new_alarm = AlarmClock ()
print (new_alarm.current_time)
print (new_alarm.alarm_time_to_sound)
print (new_alarm.is_alarm_set)

new_alarm.set_current_time()
print(new_alarm.current_time)

new_alarm.set_alarm_time_to_sound()
print (new_alarm.alarm_time_to_sound)

new_alarm.toggle_alarm_on_off()

print (new_alarm.is_alarm_set)