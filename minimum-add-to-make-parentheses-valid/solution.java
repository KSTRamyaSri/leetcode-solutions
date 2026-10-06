// =====================================================
// Approach 1 — Original Approach
// =====================================================

class Solution {
    public int minAddToMakeValid(String s) {
        int oc=0, cc=0;
        for(int i=0; i<s.length(); i++)
        {
            //needed bettere version
            //some what more
            //can u
            if(s.charAt(i)== '(')   oc++;
            else{
                if(oc>0)oc--;
                else cc++;
            }
        }
        return oc+cc;
    }
}

