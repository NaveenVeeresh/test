def hello(name, lang):
    greetings = {
        "English": "Hello",
        "Spanish": "halo",
        "German": "hallo"
    }
    msg = f"{greetings[lang]} {name}"
    print(msg)


if __name__ == "__main__":
    import argparse

    #as the name says, its command line args
    #required means mandatory =true

    parser = argparse.ArgumentParser(
        description="Provides a personal greeting"
    )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="the name of person to greet"
    )

    parser.add_argument(
        "-l", "--language", metavar="Language",
        required=True, choices=["English","Spanish","German"],
        help="language with a greeting"
    )

    args = parser.parse_args()
    hello(args.name,args.language)