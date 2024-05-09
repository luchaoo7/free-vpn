class SubscriptionHelper2(SubscriptionHelper):
    def cc_okay(self,cc ):
        return (True, None)
        
    def scheduleNextUpdate(self):
        if self.state.isAgentDisabled():
            if DEBUG >= 1:
                print("Subscription is disabled, not scheduling update")
            return
        nextUpdate = self.state.getNextUpdateTime()
        timeUntilNextUpdate = nextUpdate - time.time()
        if DEBUG:
            print("Scheduling next subscription update in %ds" % timeUntilNextUpdate)
        if timeUntilNextUpdate < 1:
            timeUntilNextUpdate = 1
        self._cancel_update_timer()
        # self.update_timer = reactor.callLater(timeUntilNextUpdate, self._update_subscription_server)

class SubscriptionTracking2(SubscriptionTracking):
    def __init__(self):
        super().__init__()
        self.initValues()

    def initValues(self, initTime=None):
        self.agent_id = None
        self.updates_failed = 0 
        self.lastUpdate = 0 
        self.cc_limit = 5 
        self.next_update = 1800
        self.min_update = 5 
        self.state = "NO_REPLY"
        self.notes = ""
        self.cc_reported = False
        self.fallback_cc = 5 
        self.agent_timeout = 12
        self.errormsg = None
        self.subscription_name = "(no subscription)"
        self.subscription_type = "-" 
        self.subscription_maxcc = -1
        self.subscription_totalcc = -1
        self.validation_timeout = 30
        self.inOverdraft = False
        self.local_cc_limit = -1
        self.lastValidUpdate = None
        if initTime == None:
            initTime = time.time()
        self.initTime = initTime

    def set_concurrent_connection(self, new_cc):
        self.cc = new_cc
        return False
    
    def clearAgentParamters(self):
        self.initValues()
        self.cc_limit = 5
        self.fallback_cc = 5

    def getCurrentCCLimit(self):
        return 5
    
    def check_cc(self, cc):
        return True
    
    def set_concurrent_connection(self, new_cc):
        if self.cc != new_cc:
            self.cc_reported = True
        self.cc = new_cc
        return False