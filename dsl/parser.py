import tatsu

SNACTOR_DSL_GRAMMAR = '''
    @@grammar::snactordsl

    # RULES

    start 
        = actor_type name blockopen actor_body blockclose $ ;

    actor_body
        =
        | inrule actor_body
        | outrule actor_body
        | inrule
        | outrule
        ;

    inrule
        = in blockopen inbody blockclose ;

    outrule
        = out blockopen outbody blockclose ;

    inbody
        = 
        | inchannel inbody
        | inchannel 
        ;
    
    outbody
        = 
        | outchannel outbody
        | outchannel 
        ;
        
    inchannel
        = channel name ;
    
    outchannel
        = channel name equal producer ;

    channel
        = name lp versions rp ;

    producer
        = producer_type lp path rp ;

    path
        = stropenclose string stropenclose ;

    versions 
        = 
        | version comma versions
        | version
        ;

    # TOKENS
    
    actor_type 
        = 
        | 'scan'
        | 'modify'
        ;

    blockclose
        = '}' ;

    blockopen
        = '{' ;

    comma
        = ',' ;

    equal
        = '=' ;

    in
        = 'in' ;

    lp
        = '(' ;
    
    name
        = /[a-zA-Z][\w]+/ ;

    out
        = 'out' ;
    
    producer_type
        = 
        | 'python'
        | 'shell'
        ;

    rp 
        = ')' ;

    string =
        /[^"']*/ ;

    stropenclose
        =
        | '"'
        | "'" 
        ;

    version
        = /[\w\d\.]+/ ;

'''

## IDEAS TO ADD:
## Since every script should return json, we can add selectors which will be aplied on top of
## returned data. I. e. 
## Type Name = python("script_name.py").section
## where .section can be chained

## ADD var section / inline + block
## This will allow us to set a variable / execute a script and then disect the output of it in "out" section


## The test_out must be exported by get_test_out.py otherwise the output will be undefined
## In case there will be multiple outputs from the same script, it will be aggragated & executed only once
## Example: Execution of:
##   TestOut(0.1) out1 = python("get_outputs.py)
##   TestOut(0.1) out2 = python("get_outputs.py)
## will result into one time execution of get_outputs.py and then disecting it (basically the same way it is done now,
## either it is exported or not).
definition = """
scan portscan {
    in {
        Test(0.1,0.2,0.3) test_in
        TestW(0.1) test_in2
    }
    
    out {
        TestOut(0.1) test_out = python('get_test_out.py')
    }
}
"""

a = tatsu.parse(SNACTOR_DSL_GRAMMAR, definition)
from pprint import pprint
print(definition)
pprint(a)
