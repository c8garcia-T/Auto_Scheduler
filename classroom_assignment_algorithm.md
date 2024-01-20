## Data Schema
- Grade Level: Str (Category)
- Class Label: Str (Category)
- Student Count in Class Label : Int (Fixed)
- Class Room : Int (Fixed)
- Teacher : Str (Category)
- Course Name: Str (Category)
- Time of Course: DateTime 


### Sample Schedule:
    Elementary Grade               | Middle School Grade
    Class Label #1 , Class Label #2 | Class Label #3
    2                   7               10
    12:00: None              T_A-CN-RM5      | T_X-CN-RM4
    13:00  T3-CN-RM3         T_B-CN-RM9     | T_C- CN-RM1
    14:00   T3-CN-RM3        T_D-CN-RM10    | None
    15:00           T_H-CN-RM3               | T_F - CN-RM4

Abbreviations
T = Teacher
CN = Course Name
RM = Room Number

Problem can be treated like filling in an nxn matrix appropriately. 
- N rooms available. 
- 2-10pm Time Range. 
- Given time T there are N Classes
  - Class 'x' has N Students 
- Class 'x' also has Class 'y(s)' after

# Problem:
1. Given N number of Class Rooms 0 to N, Fill them in with Course X to Z. 
#### Facts:
1. Num of Courses <= Num of Class Rooms 
## Solutions
##### Data Structure: List(Classroom #) , List(Courses)
### Sequantial Fill 
1. Iterate from List ('Courses') and assign them to an available Classroom #. 
#### Data Structure Variant (all solutions): Based on Preference
1. Sort List('Courses') Based on Teacher room # Preference
#### Conditional (all solutions): Based on Class Size
1. If classroom # (number of available seats) < 'Course' ('number of students present') skip classroom # else assign
2. Sequential Solution Choice
#### Sequential Variant: Random
1. Shuffle List('Courses') 
2. Original Step #1
#### Conditional (all solutions): Reason Based Classroom # Seperation
1. if classroom # Current - 1 == 'reason' or if classroom # Current + 1 == 'reason': then skip classriin # else assign 
2. Solution Choice
- Reasons: Loudness, Grade Level (Ease of Accessibility), other
#### Conditional (all solutions): Reason Based Classroom # Neighbor
1. if classroom # Current - 1 == 'reason' or if classroom # Current + 1 == 'reason': then assign else skip 
2. Solution Choice
- Reasons: Help, Next Class Proximity, other
#### Data Structure Variant (all solutions): Sort Classroom # Based on # of Available Seats
1. sort classroom # based on # of available seats
#### Data Structure Variant (all solutions): Sort Courses  Based on Presence of Separation/Neighbor/preference rigidity 
1. sort Courses based on whether 'preference', or 'separation/neighbor' request is rigid.

## Proposed Solution:
- Data Structure Sorted List( Sort Classroom # Based on available # of seats)
- Data Sructure List(Courses Sorted based on [(Separation/Neighbor), preference] Requirement Prescence)
    Error Handling
    1. WIP
1. Conditional (Class Size)
2. Conditional (Reason Based Separation)
3. Conditional (Reason Based Neighbor)
4. Sequantial Fill 