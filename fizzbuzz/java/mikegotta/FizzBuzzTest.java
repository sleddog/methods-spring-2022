/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package fizzbuzz;

import org.junit.Test;
import static org.junit.Assert.*;

/**
 *The FizzBuzzTest class tests all possible combinations of the multiples
 * of 3, 5, 7, and 11 to check that the FizzBuzz program returns the 
 * correct string value for the number sent in.
 */
public class FizzBuzzTest {

    @Test
    public void testMultiplesOf3() {
        FizzBuzz FizzBuzz = new FizzBuzz();
        assertEquals("Fizz", FizzBuzz.fizzBuzz(6));
    }
    
    @Test
    public void testMultiplesOf5() {
        assertEquals("Buzz", FizzBuzz.fizzBuzz(10));
    }
    
    @Test
    public void testMultiplesOf7() {
        assertEquals("Ping", FizzBuzz.fizzBuzz(14));
    }
    
    @Test
    public void testMultiplesOf11() {
        assertEquals("Pong", FizzBuzz.fizzBuzz(22));
    }
    
    @Test
    public void testMultiplesOf3And5() {
        assertEquals("FizzBuzz", FizzBuzz.fizzBuzz(15));
    }
    
    @Test
    public void testMultiplesOf3And7() {
        assertEquals("FizzPing", FizzBuzz.fizzBuzz(21));
    }
    
    @Test
    public void testMultiplesOf3And11() {
        assertEquals("FizzPong", FizzBuzz.fizzBuzz(33));
    }
    
    @Test
    public void testMultiplesOf5And7() {
        assertEquals("BuzzPing", FizzBuzz.fizzBuzz(35));
    }
    
    @Test
    public void testMultiplesOf5And11() {
        assertEquals("BuzzPong", FizzBuzz.fizzBuzz(55));
    }
    
    @Test
    public void testMultiplesOf7And11() {
        assertEquals("PingPong", FizzBuzz.fizzBuzz(77));
    }
    
    @Test
    public void testMultiplesOf3And5And7() {
        assertEquals("FizzBuzzPing", FizzBuzz.fizzBuzz(105));
    }
    
    @Test
    public void testMultiplesOf3And5And11() {
        assertEquals("FizzBuzzPong", FizzBuzz.fizzBuzz(165));
    }
    
    @Test
    public void testMultiplesOf3And7And11() {
        assertEquals("FizzPingPong", FizzBuzz.fizzBuzz(231));
    }
    
    @Test
    public void testMultiplesOf5And7And11() {
        assertEquals("BuzzPingPong", FizzBuzz.fizzBuzz(385));
    }
    
    @Test
    public void testMultiplesOf3And5And7And11() {
        assertEquals("FizzBuzzPingPong", FizzBuzz.fizzBuzz(1155));
    }
    
}

    

