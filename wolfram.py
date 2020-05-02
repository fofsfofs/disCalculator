import wolframalpha

wolfclient = wolframalpha.Client("L766YW-6V34XVRVWG")

def query(command, expression):
    res = wolfclient.query("{} {}".format(command,expression))
    return next(res.results).text
