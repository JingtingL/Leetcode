class Solution {
public:
    int reverse(int x) {
        string string_x = to_string(x);
        string sign = "";
        string string_rst = "";

        for (int index = 0; index<string_x.size(); index++){
            if (index == 0 && string_x[index] == '-'){
                sign = string_x[0];
                continue;
            }

            string_rst = string_x[index] + string_rst;
        }

        if (sign == "-"){
            string_rst = sign + string_rst;
        }

        long long value = stoll(string_rst);
        return (-2147483648LL <= value && value <= 2147483647LL) ? int(value) : 0;
    }
};