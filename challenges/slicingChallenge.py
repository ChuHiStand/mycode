#!/usr/bin/env python3

challenge = ["science", "turbo", ["goggles", "eyes"], "nothing"]
challenge_goggles = challenge[2][0]
challenge_eyes = challenge[2][1]
challenge_nothing = challenge[3]
print("My " + challenge_eyes + "! " + "The " + challenge_goggles + " do " + challenge_nothing + "!")

trial = ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]
trial_eyes = trial[2]["goggles"]
trial_goggles = trial[2]["eyes"]
trial_nothing = trial[3]
print("My " + trial_eyes + "! " + "The " + trial_goggles + " do " + trial_nothing + "!")


nightmare = [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]
nightmare_eyes = nightmare[0]["user"]["name"]["first"]
nightmare_goggles = nightmare[0]["kumquat"]
nightmare_nothing = nightmare[0]["d"]
print("My " + nightmare_eyes + "! " + "The " + nightmare_goggles + " do " + nightmare_nothing + "!")



