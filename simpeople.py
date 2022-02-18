# Used to store and manage information related to an airline passenger.
class Passenger :
   # Creates a passenger object.
  def __init__( self, id_num, arrival_time ):
    self._id_num = id_num
    self._arrival_time = arrival_time

   # Gets the passenger's id number.
  def id_num( self ) :
    return self._id_num 
    
   # Gets the passenger's arrival time.
  def time_arrived( self ) :
    return self._arrival_time 
    
# Used to store and manage information related to an airline ticket agent.
class TicketAgent :
   # Creates a ticket agent object.
  def __init__( self, id_num ):
    self._id_num = id_num
    self._passenger = None
    self._stop_time = -1
    
   # Gets the ticket agent's id number.
  def id_num( self ):
    return self._id_num 
    
   # Determines if the ticket agent is free to assist a passenger.
  def is_free( self ):
    return self._passenger is None 
      
   # Determines if the ticket agent has finished helping the passenger.
  def is_finished( self, cur_time ):
    return self._passenger is not None and self._stop_time == cur_time
    
   # Indicates the ticket agent has begun assisting a passenger.
  def start_service( self, passenger, stop_time ):
    self._passenger = passenger
    self._stop_time = stop_time
    
   # Indicates the ticket agent has finished helping the passenger.
  def stop_service( self ):
    the_passenger = self._passenger
    self._passenger = None
    return the_passenger
    
