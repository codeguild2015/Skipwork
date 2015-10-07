""" 
Exercise
With your partner:
Create a new class, SMS_store. The class will instantiate SMS_store 
objects, similar to an inbox or outbox on a cellphone:

my_inbox = SMS_store()

This store can hold multiple SMS messages (i.e. its internal state 
will just be a list of messages). Each message will be represented 
as a tuple:
(has_been_viewed, from_number, time_arrived, text_of_SMS)
The inbox object should provide these methods:" """

class SMS_store

my_inbox = SMS_store()

message = (from_number, time_arrived, text_of_SMS)

    def __init__(self, var):
        self.inbox = []
		
    def my_inbox.add_new_arrival(from_number, time_arrived, text_of_SMS)
	    has_been_viewed = False
		msg = (has_been_viewed, from_number, time_arrived, text_of_SMS)
        self.inbox.append()
	
    def my_inbox.message_count()
        
        	

	
	
    def add_one():
	    self.inbox.append()
		
    def add_something(self, something)
	     self.inbox.append(something)
		
	

def my_inbox.add_new_arrival(from_number, time_arrived, text_of_SMS)
    # Makes new SMS tuple, inserts it after other messages
    # in the store. When creating this message, its
    # has_been_viewed status is set False.

def my_inbox.message_count()
    # Returns the number of sms messages in my_inbox

def my_inbox.get_unread_indexes()
    # Returns list of indexes of all not-yet-viewed SMS messages

def my_inbox.get_message(i)
    # Return (from_number, time_arrived, text_of_sms) for message[i]
    # Also change its state to "has been viewed".
    # If there is no message at position i, return None

my_inbox.delete(i)     # Delete the message at index i
my_inbox.clear()       # Delete all messages from inbox