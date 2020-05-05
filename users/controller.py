from users.models import *
class UserController():
    def __init__(self,user):
        self.id = user.id
        self.userDetail = UserDetail.objects.get( user = self.id )
        self.user = user
    def getUserSchool(self):
        return self.userDetail.school.school_name
    def getUserSex(self):
        return self.userDetail.sex
