class User:
    def init(self):
        self.User_Id = 0
        self.Username = ""
        self.Description = ""
        self.Password = ""

class Leaderboard:
    def init(self):
        self.Lb_Id = 0
        self.User_Id = 0
        self.Name = ""
        self.Description = ""

class Ranking:
    def init(self):
        self.Ranking_Id = 0
        self.Lb_Id = 0
        self.Name = ""
        self.Score = ""