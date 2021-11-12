import numpy as np

def main():
    B = 7

    ids = [
        '331', '332', '330', '314', '378',
        '319', '320', '379', '315', '333',
        '321', '380', '316', '335', '381',
        '381', '100', '382', '322', '061',
        '336', '337', '317', '383', '384', '385']
    dd1 = list(map(lambda x: (int(x[0]) + B) % 10, ids))
    avg1 = np.mean(dd1)
    dd2 = list(map(lambda x: (int(x[1]) + B) % 10, ids))
    avg2 = np.mean(dd2)
    dd3 = list(map(lambda x: (int(x[2]) + B) % 10, ids))
    avg3 = np.mean(dd3)
    print('Average for 1st digits is {}'.format(avg1))
    print('Average for 2nd digits is {}'.format(avg2))
    print('Average for 3rd digits is {}'.format(avg3))

    print('Overall goodness = {}'.format(abs(avg2 - 5) + abs(avg3- 5)))



if __name__ == '__main__':
    main()