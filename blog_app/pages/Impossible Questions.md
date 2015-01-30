# Impossible Questions

Just a minor disclaimer before I begin: I don't hold a formal degree in anything, and this isn't an authoritative 
source. It's just me having fun! :)


I was recently asked to interview for a very well known software company. I was super excited for the opportunity 
(crazy awesome perks!) and ready for some fun programming challenges. I'm not an expert programmer by any stretch, 
but boy do I enjoy solving problems!
 
 Before I talk about the interview and the questions, I'd like to briefly touch base on something called The Shannon Limit. 
Don't take this as a formal statement of everything that Shannon covered, but for my purposes we should keep this in mind:
 To state things simply, The Shannon Limit is the limit of the amount of information that can be stored in a fixed finite 
  amount of bits. Sounds pretty intuitive and reasonable, right? 
  
So, that gives us our first assertion: One bit of information can only store two states: 1 and 0. 

That's great! Well, what if we add a second bit? It turns out that this doubles our capacity for storage. For 
those of you who know binary, this is painfully obvious: two bits gives us four states, three gives us eight, and so on.

The binary number 111 gives us much more information than three separate bits could. 
The reason for this is that the _position_ of the bits is another way to store information. As we change position in
 binary we aren't increasing the amount of storage by ten as we would in decimal, but instead by an order of 2.

Thus, our second assertion: For each added bit we double the total amount of information that we can store. 
  
Now it looks like we're getting somewhere! But, do we always need all those bits? Can't 10000000000 somehow be cleverly 
 represented as 1 with 1010 zeros? Can't every number?


As it turns out, if we were to randomly generate a fixed amount of bits
 and then we were to try to come up with a way to represent that _same_ information but using fewer bits (compress them)
 , we wouldn't be 
 reducing our number very much at all. It's always possible that we could find numbers that give us interesting patters:
 nice squares (or close to them), numbers with a lot of trailing zeros (scientific notation) and so on. However,
 on average (if we have no control of the numbers we get), we will need the same amount of bits to represent our 
 information no matter the compression chosen: Shannon covered this in his famous paper: [A Mathematical Theory of Communication](http://cm.bell-labs.com/cm/ms/what/shannonday/shannon1948.pdf). 
  
 For our purposes we can build our third assertion: When given some bits we won't be able to significantly reduce the 
 amount of bits without losing information.
  
  
 So that covers that so far! What does this have to do with programming interviews? Well, it turns out our problem to solve
  was, in a way, related to Shannon's Limit.
   
   
The scene:

A person in their livingroom opens their TV guide. They notice on the left of the guide is a series of numbers in decimal,
  all listed under a column titled "record code." Interested in what this means, this person calls up the company 
  responsible for the TV guide and gets a support representative on the phone.
  
"Hello! Thank you for calling TV Guide. My name is John. How can I help you?"

The man gives his query, "The numbers on the right, where it says 'record code,' what does this mean?"

Which drives the support representative into a sales pitch to sell their awesome new VCRs with smart-recording! 
 Just plug the number and the VCR starts recording for you!
 
