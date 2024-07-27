function isValid(s: string): boolean {
    const stack: string[] = [];

    for (let current of s) {
        switch (current) {
            case '(':
            stack.push(current);
            break;
            case '{':
            stack.push(current);
            break;
            case '[':
            stack.push(current);
            break;
            case ')':
            if (stack.pop() != '(') return false;
            break;
            case '}':
            if (stack.pop() != '{') return false;
            break;
            case ']':
            if (stack.pop() != '[') return false;
            break;
        }
    }

  return stack.length == 0;  
};