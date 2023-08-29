class ChoiceDisplayer:
    def __init__(self, user):
        self.user = user

    def __str__(self):
        return (f"""
                    user_name - {self.user.user_name}
                    user_id - {self.user.user_id}
                    group - {self.user.group_id}
                    role - {self.user.role}
                """)