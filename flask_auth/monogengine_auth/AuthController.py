from flask import Response, request

class Authorization:
    def __init__(self, model):
        self.model = model
    
    def isAllowed(self, base_function):
        def authentication(*args, **kwargs):    
            return self.__token_verification(base_function, 'isAllowed', *args, **kwargs)
        return authentication
    
    def isAdmin(self, base_function):
        def authentication(*args, **kwargs):    
            return self.__token_verification(base_function, 'isAdmin', *args, **kwargs)
        return authentication
    
    def isStaff(self, base_function):
        def authentication(*args, **kwargs):    
            return self.__token_verification(base_function, 'isStaff', *args, **kwargs)
        return authentication
    
    def isPublic(self, base_function):
        def authentication(*args, **kwargs):    
            return self.__token_verification(base_function, 'isPublic', *args, **kwargs)
        return authentication
    
    def login(self, username=None, password=None):
        try:
            user = self.model.objects.get(username=username)
            if user.verify_password(password):
                token = user.create_token()
                user.save()
                return {
                    "user":user,
                    "token":token,
                    'error':False,
                    "message":'Login Successful'
                }
            else:
                return {
                    "error":True,
                    "message":"Provided credentials does not match"
                }
        except Exception as e:
            return {
                "error":True,
                "message":"User not found"
            }

    def __token_verification(self, base_function, type, *args, **kwargs):
        token = request.headers.get("Authorization", None)
        if token:
            token = self.model.verify_token(token)
            try:
                user = self.model.objects.get(token=token)

                if type == 'isAdmin':
                    return self.__isAdminCheck(base_function, user, *args, **kwargs)
                elif type == 'isStaff':
                    return self.__isStaffCheck(base_function, user, *args, **kwargs)
                elif type == 'isPublic':
                    return self.__isPublicCheck(base_function, user, *args, **kwargs)
                else:
                    return self.__isAllowedCheck(base_function, user, *args, **kwargs)
            except Exception as e:
                return Response('Unauthorized', 401)
        else:
            return Response('Unauthorized', 401)
        
    def __isAllowedCheck(self, base_function, user, *args, **kwargs):
        if user.is_active:
            kwargs['user'] = user
            return base_function(*args, **kwargs)
        return Response('Unauthorized', 401)
    
    def __isAdminCheck(self, base_function, user, *args, **kwargs):
        if user.is_active and user.admin:
            kwargs['user'] = user
            return base_function(*args, **kwargs)
        return Response('Unauthorized', 401)
    
    def __isStaffCheck(self, base_function, user, *args, **kwargs):
        if user.is_active and user.staff:
            kwargs['user'] = user
            return base_function(*args, **kwargs)
        return Response('Unauthorized', 401)

    def __isPublicCheck(self, base_function, user, *args, **kwargs):
        if user.is_active and user.public:
            kwargs['user'] = user
            return base_function(*args, **kwargs)
        return Response('Unauthorized', 401)