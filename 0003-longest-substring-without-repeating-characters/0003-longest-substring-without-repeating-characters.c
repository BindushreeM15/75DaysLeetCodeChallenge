int lengthOfLongestSubstring(char* s) {
    int maxLen = 0;
    int start = 0;
    int lastIndex[256];  // For all ASCII characters
    for (int i = 0; i < 256; i++) {
        lastIndex[i] = -1;
    }

    for (int end = 0; s[end] != '\0'; end++) {
        char ch = s[end];
        if (lastIndex[ch] >= start) {
            start = lastIndex[ch] + 1;
        }
        lastIndex[ch] = end;
        int currentLen = end - start + 1;
        if (currentLen > maxLen) {
            maxLen = currentLen;
        }
    }

    return maxLen;
}
