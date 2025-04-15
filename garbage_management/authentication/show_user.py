#  context processor  - is a function that pass a http request as parameter and return a data in dictionary format

# here context processor is used to implement how a username displays


def show_user_name(request):

    username = request.user.username

    name = username.split('@')[0]

    print(name)

    return{'name_of_user':name}

