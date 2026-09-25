import yaml


def load_companies():
    with open("config/companies.yaml", "r") as file:
        config = yaml.safe_load(file)

    return config["companies"]




def load_profile():
    with open("config/profile.yaml", "r") as file:
        config = yaml.safe_load(file)

    return config