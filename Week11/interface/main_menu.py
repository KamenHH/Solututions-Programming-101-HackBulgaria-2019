class MainMenu:
    
    OPTION_MENU = {
        '1': show_members,
        '2': available_slots
    }


    @classmethod
    def show_options(cls, curr_user):
        option = input()
        if option == '1':
            member = MainController.show_members(curr_user)
            cls._pretty_print_members(member)

    @classmethod
    def _pretty_print_members(cls, members):
        for member in members:
            print(f'{getattr(member, 'status', '')} {member.username}')