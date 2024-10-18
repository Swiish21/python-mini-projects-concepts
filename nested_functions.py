def nstd_fcn(a, b):
    answer = a + b
    def double_answer():
        double_sum = answer*2
        print(double_sum)
    double_answer()
    return answer
print(nstd_fcn(2,2))