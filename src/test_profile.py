from config_loader import load_profile


profile = load_profile()

print("Candidate:", profile["candidate"]["name"])
print("Experience:", profile["candidate"]["experience_years"])
print("Primary skills:", profile["skills"]["primary"])
print("Target roles:", profile["target_roles"])