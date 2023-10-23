def main():
    """
    ##################################################
    Comlete your code here
    Use m_perc and f_perc for your results
    ##################################################
    """
    fnum = int(input('Enter the number of the female students: '))
    mnum = int(input('Enter the number of the male students: '))
    total = fnum + mnum
    m_perc = mnum / total * 100
    f_perc = fnum / total * 100

    print (f'The percentage of male student is {m_perc:.2f}%')
    print (f'The percentage of female student is {f_perc:.2f}%')
    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return m_perc, f_perc


if __name__ == '__main__':
    main()
