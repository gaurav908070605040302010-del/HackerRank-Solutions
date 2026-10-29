// ──────────────────────────────────────────────────
// Link        https://www.hackerrank.com/challenges/java-loops/problem?isFullScreen=true
// Problem     Java Loops II
// Difficulty  Easy
// Subdomain   Introduction
// Platform    HackerRank
// Language    java
// Status      Accepted
// Submitted   2026-10-29, 11:37 p.m.
// ──────────────────────────────────────────────────

import java.util.*;
import java.io.*;

class Solution{
    public static void main(String []argh){
        Scanner in = new Scanner(System.in);
        int t = in.nextInt(); // number of queries 'q'
        for(int i = 0; i < t; i++){
            int a = in.nextInt();
            int b = in.nextInt();
            int n = in.nextInt();
            
            int currentSum = a;
            for(int j = 0; j < n; j++) {
                currentSum += (int)(Math.pow(2, j) * b);
                System.out.print(currentSum + " ");
            }
            System.out.println();
        }
        in.close();
    }
}
