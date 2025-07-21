def mdp():
    mdp = input("Please enter the MDP value: ")
    while not mdp:
        print("No MDP value provided. Please try again.")
        mdp = input("Please enter the MDP value: ")
    return mdp


if __name__ == "__main__":
    result = mdp()
    print(f"Mot de passe saisi : {result}")
