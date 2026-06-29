def ask_text(ans):
    return input(ans)
def ask_int(ans):
    return int(input(ans))
def info(): #sai
    name=ask_text("enter your name -->")
    age=ask_int("enter your age -->")
    city=ask_text("enter your city -->")
    language=ask_text("enter your fav coding language -->")
    year=ask_int("from how many years are you coding -->")
    age=(f"{age}")
    year=(f"{year}")
    bio="name         :"+name+"\n"+"age          :"+age+"\n"+"city         :"+city+"\n"+"fav language :"+language+"\n"+"coding from "+year+"years"+"\n"
    return bio,name
def greeter(name):
    return f"hey {name}, nice to meet you"
def main():
    bio,name=info() #sai
    headline=greeter(name)
    print(headline)
    print("="*40,"\n","                ABOUT ME","\n",'='*39)
    print(bio)
    print("="*40)
main()
