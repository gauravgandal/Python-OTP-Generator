import math, random, time
import string
def get_string(lower,upper, digits_count,special_count):
    lower = ''.join((random.choice(string.ascii_lowercase) for i in range(lower)))
    upper = ''.join((random.choice(string.ascii_uppercase) for i in range(upper)))
    digits = ''.join((random.choice(string.digits) for i in range(digits_count)))
    special = ''.join((random.choice(string.punctuation) for i in range(special_count)))
    sample_list = list(lower + upper + digits+special)
    random.shuffle(sample_list)
    final_string = ''.join(sample_list)
    return(final_string)
if __name__ == "__main__" :
    while True:
      print("OTP of length 6:", get_string(2,2,1,1))
      time.sleep(10)