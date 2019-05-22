# 1 - check schedule
# 2 - check reserved appointments
# 3 - check appointments for a given date
# 4 - reschedule appoinment
# 5 - exit
import sys
from utils.decorators import Clear


class DoctorController:
    def __init__(self, doctor_obj):
        self.doctor_obj = doctor_obj

    def check_schedule(self):
        pass

    @staticmethod
    def return_to_login_screen():
        print('\nGoodbye!\n')
        return None