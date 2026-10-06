// =====================================================
// Approach 1 | First Added: 06 October 2026 | Last Updated: 06 October 2026
// =====================================================

class Solution {
    public int minAddToMakeValid(String s) {
        int oc=0, cc=0;
        for(int i=0; i<s.length(); i++)
        {
            if(s.charAt(i)== '(')   oc++;
            else{
                if(oc>0)oc--;
                else cc++;
            }
        }
        return oc+cc;
    }
}
