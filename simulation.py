# Implementation of the main simulation class.
from Chapter2.myarray import Array
from llistqueue import Queue
from simpeople import TicketAgent, Passenger

import random

class TicketCounterSimulation :
   # Create a simulation object.
  def __init__( self, num_agents, num_minutes, between_time, service_time ):
     # Parameters supplied by the user.
    self._arrive_prob = 1.0 / between_time  
    self._service_time = service_time
    self._num_minutes = num_minutes         
     
     # Simulation components.
    self._passenger_q = Queue()   
    self._the_agents = Array( num_agents )    
    for i in range( num_agents ) :
      self._the_agents[i] = TicketAgent(i+1)
    
     # Computed during the simulation.
    self._total_wait_time = 0
    self._num_passengers = 0
    
   # Run the simulation using the parameters supplied earlier.
  def run( self ):
    for cur_time in range(self._num_minutes + 1) :
      self._handle_arrival( cur_time ) 
      self._handle_begin_service( cur_time )      
      self._handle_end_service( cur_time )

   # Print the simulation results.
  def print_results( self ):
    num_served = self._num_passengers - len(self._passenger_q)
    avg_wait = float( self._total_wait_time ) / num_served
    print( "" )
    print( "Number of passengers served = ", num_served )
    print( "Number of passengers remaining in line = %d" %
           len(self._passenger_q) )
    print( "The average wait time was %4.2f minutes." % avg_wait ) 
   
  # The remaining methods that have yet to be implemented.
  # def _handle_arrive( cur_time ):        # Handles simulation rule #1.
  # def _handle_begin_service( cur_time ):  # Handles simulation rule #2.
  # def _handle_end_service( cur_time ):    # Handles simulation rule #3.

  def _handle_arrival( self, cur_time ):
    p = random.random()
    if p < self._arrive_prob:    # a passenger should arrive
      passenger = Passenger( self._num_passengers, cur_time )
      self._passenger_q.enqueue( passenger )

      print( 'Time ', cur_time, ': Passenger ', \
               self._num_passengers, ' arrived.' ) 

      self._num_passengers += 1

  def _handle_begin_service( self, cur_time ):
    if self._passenger_q.isEmpty() == False:    # handle a customer
      agent_ID = self._find_free_agent()
      if agent_ID >= 0:    # found a free one
        this_passenger = self._passenger_q.dequeue()
        stop_time = cur_time + self._service_time
        self._the_agents[ agent_ID ].start_service( this_passenger, stop_time )

        self._total_wait_time += cur_time - this_passenger._arrival_time

        print( 'Time ', cur_time, ': Agent ', agent_ID, \
                 ' started serving passenger ', this_passenger.id_num(), '.' )

  def _handle_end_service( self, cur_time ):
    agent_ID = self._find_finish_agent( cur_time )
    if agent_ID >= 0:    # found one who should complete the service
      this_passenger = self._the_agents[ agent_ID ].stop_service()
      
      print( 'Time ', cur_time, ': Agent ', agent_ID, \
                 ' stopped serving passenger ', this_passenger.id_num(), '.' )

  def _find_free_agent( self ):
    for i in range( len( self._the_agents ) ):
      if self._the_agents[ i ].is_free():
        return i   # found a free one
    return -1      # no free agent is found

  def _find_finish_agent( self, cur_time ):
    for i in range( len( self._the_agents ) ):
      if self._the_agents[ i ].is_finished( cur_time ):
        return i   # found a finished one
    return -1      # no finished agent is found
    

def main():
  num_agents = 2
  total_sim_time = 200
  interarrival_time = 5
  service_time = 6

  bison_airline_agency = TicketCounterSimulation( \
    num_agents, total_sim_time, interarrival_time, service_time )

  print( 'Number of Agents: ', num_agents )
  print( 'Total Sim Time: ', total_sim_time )
  print( 'Interarrival Time: ', interarrival_time )
  print( 'Service Time: ', service_time )
  bison_airline_agency.run()
  bison_airline_agency.print_results()

main()
