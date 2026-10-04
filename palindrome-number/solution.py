class Solution {
    public boolean isPalindrome(int x) {
        if(x<0) return false;

        int y = x;
        long  revx = 0;
        while(y>0)
        {
            int digit = y%10;
            revx = revx*10+digit;
            y = y/10;
        }
        if(revx == x) return true;
        return false;
    }
}

# =====================================================
# Approach 2
# =====================================================

class Solution {
    public boolean isPalindrome(int x) {
        if(x<0) return false;

        // attempt 2
        int y = x;
        long  revx = 0;
        while(y>0)
        {
            int digit = y%10;
            revx = revx*10+digit;
            y = y/10;
        }
        if(revx == x) return true;
        return false;
    }
}

# =====================================================
# Approach 3
# =====================================================

class Solution {
    public boolean isPalindrome(int x) {
        if(x<0) return false;

        // attempt 2
        int y = x;
        long  revx = 0;
        while(y>0)
        {
            int digit = y10;
            revx = revx*10+digit;
            y = y/10;
        }
        if(revx == x) return true;
        return false;
    }
}

# =====================================================
# Approach 4
# =====================================================

class Solution {
    public boolean isPalindrome(int x) {
        if(x<0) return false;

        // attempt 4
        int y = x;
        long  revx = 0;
        while(y>0)
        {
            int digit = y%10;
            revx = revx*10+digit;
            y = y/10;
        }
        if(revx == x) return true;
        return false;
    }
}

# =====================================================
# Approach 5
# =====================================================

class Solution {
    public boolean isPalindrome(int x) {
        if(x<0) return false;

        // attempt 5 checkingggg
        int y = x;
        long  revx = 0;
        while(y>0)
        {
            int digit = y%10;
            revx = revx*10+digit;
            y = y/10;
        }
        if(revx == x) return true;
        return false;
    }
}

# =====================================================
# Approach 6
# =====================================================

class Solution {
    public boolean isPalindrome(int x) {
        if(x<0) return false;
    //atte,pt s6
        // attempt 5 checkinggggdddddddddddddddddddddddddgdgdsgfdsgtergt 
        int y = x;
        long  revx = 0;
        while(y>0)
        {
            int digit = y%10;
            revx = revx*10+digit;
            y = y/10;
        }
        if(revx == x) return true;
        return false;
    }
}
