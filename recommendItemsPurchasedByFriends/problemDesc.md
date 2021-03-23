--This problem is from interviewing.io
--mock interview
--DFS
--Graph

#include <iostream>
using namespace std;

// To execute C++, please define "int main()"
int main() {
  auto words = { "Hello, ", "World!", "\n" };
  for (const string& word : words) {
    cout << word;
  }
  return 0;
}


/* 

An online retailer is releasing a new feature called "What are my friends
buying?". The feature lists a set of products that you have not already
purchased from the things that your friends have bought, in order of most bought
to least bought.

To help with this, we have the following 2 APIs. Complete the function that
takes in a person and returns the items that the person's friends are buying.

```
// Returns a list of Items purchased by a Person. If purchased multiple times, an
// Item will be in the list multiple times.
List<Item> getPurchases(Person person);

// Returns a list of friends of a Person.
List<Person> getFriends(Person person);
``

---

Instead of your friends, what about your social circle? A social circle of a person is defined as the person's friends and their friends.

A->B, 

A-> B, C, D
B-> E, F, D

keep a unique list (dictionary) 
A, B, C, D

B-> E, F,
---

---

Recently we've discovered that individuals with high number of purchases for a single item can skew the results. Now we want to count each purchase by a person exactly once. How do we change the algorithm?

--

Problem Description
1. Feature: We want to get the list of products that someone's friends are buying,
2. The recommended products are not bought by current person.
3. The return list should be sorted by freq from high to low.

4. API: given a person, return list of products
5. API: given a person, return friend list.

Ask: 
vector<Item> recommededProducts(Person person) {
  
}

Constraints:
1. return all items that are purchased by friends

Example:
A-> B, C

Products:
A-> 0, 1, 2, 3
B-> 3, 4, 5, 6, 6, 
C-> 7, 8, 9 ,0, 7

A-> 4, 5, 6, 7, 8, 9

mapping of item->count
0->3, 3->2, 7-2

Data structure:
1. Dictionary to store items, (unique list of items that current person purchased)
2. Dictionary to store mapping of item->count_of_purchases
3. Use a Priority_Que pair <cnt, item_id> : keep it sorted based on freq

A-> query friend list-> B, C, B->products

N = total friends
M = total number of items purchased by person/friends
U = unique number of items

Time: N + M + U + UlogU = O(N + M + UlogU)
Space: U + U = O(U)


//getPurchases(Person person);
//getFriends(Person person)

Products:
A-> 0, 1, 2, 3, 0
B-> 3, 4, 5, 6, 6, 
C-> 7, 3, 4 ,0, 7

A-> 4, 5, 6, 7, 8, 9

mapping of item->count
0->3, 3->2, 7-2
  
*/
vector<Item> recommededProducts(Person person) { //Person A
  unordered_map<Item, int> item2cnt;
  //step1
  unordered_set<Item> purchased;
  for (auto item: getPurchases(person)) { // 0, 1, 2, 3, 0
    item2cnt[item] += 1;              // 0->2, 1->1, 2->1, 3->1
    purchased.insert(item);  //0, 1, 2, 3
  }
  
  //step2
  
  
  for (auto frnd: getFriends(person)) { //B, C
    for (auto item: getPurchases(frnd)) { //B: 3,4,5,6,6, C: 7, 3, 4, 0, 7
      item2cnt[item] += 1; // 0->3, 1->1, 2->1, 3->3, 4->2, 5->1, 6->2, 7->2 
    }
  }
  
  //Step3 (Building Priority Queue) 1,2,,...,N,  O(NlogN) |set
  priority_queue<pair<int, Item>> maxQ;
  for(auto e: item2cnt) {
    maxQ.push({e.second, e.first}); //(3,0), (3,3), (2,4), (2,6), (2,7), (1,2),(1,1),(1,5)
  }
  
  //step 4
  vector<Item> result; //4, 6, 7,
  while (!maxQ.empty()) {
    auto curr = maxQ.top().second;
    if (!purchased.count(curr)) {//Purchased: 0, 1, 2, 3
      result.push_back(curr);
    }
    maxQ.pop();
  }
  return result; //4, 6, 7
}

void getFriedCircle(Person person, unordered_set<Person>& cicle) {
  if (circle.count(person)) {
    return;
  }
  cicle.insert(person);
  for (auto frnd: getFriends(person)){
    getFriendCircle(frnd);
  }
}

BFS-> A
queue<Person> q;
q.insert(A);
         int level = N;
while (!q.empty() && N > 0) {
  for (int i = q.size()-1; i >= 0; --i) {
    auto person = q.top();
    q.pop();
    circle.insert(person);
    for (auto frind: getFriends(person)) 
      q.push(friend);
  }
  N -=1 ;
}
         
/*
A-> B, C, D
B-> E, F, D
F-> G, H, I
I-> Z


upto N level, explore till N level.
keep a unique list (dictionary) 
A, B, C, D

B-> E, F,
*/