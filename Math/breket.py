def chekStr(str):
    stack = []
    for val in str:
        if val == '(' or val == '[' or val == '{':
            stack.append(val)
            continue

        if not stack:
            return False

        x = stack.pop()
        if not (val == ')' and x == '(' or val == '}' and x == '{' or val == ']' and x == '['):
            return False

    return not stack

string = "{()}[}]"
print(string, "-", chekStr(string))

string = "{[]{()}}"
print(string, "-", chekStr(string))

string = "[{}{})(]"
print(string, "-", chekStr(string))


# package example;

# import java.util.Scanner;
# import java.util.Stack;

# public class l {
# public static void main(String [] args){
# Scanner myObj = new Scanner(System.in);
# String A = myObj.nextLine();
# System.out.println(stugel(A));
# }
# static boolean stugel(String A){

#     Stack<String> STACK = new Stack<String>();

#     for (char V:A.toCharArray()){
#         if(V == '(' || V == '{' || V == '['){
#             STACK.push(Character.toString(V));
#             continue;
#         }
#         if (STACK.isEmpty())
#             return false;

#         char x = STACK.pop().charAt(0);
#         if(x == '(' && V == ')' || x == '[' && V == ']' || x == '{' && V == '}')
#             continue;
#         else
#             return false;
#         }

#         return STACK.isEmpty();
#     }
# }