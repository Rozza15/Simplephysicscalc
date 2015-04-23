"""
Software Version 0.4.1
"""

"""
Simplephysicscalc is a small project to find the answers to simple physics eqautions, and will in the future likely get more updates and functions
    Copyright (C) 2015  Rory Buchanan

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

#License Details
c = "This program is free software: you can redistribute it and/or modify\
 it under the terms of the GNU General Public License as published by\
 the Free Software Foundation, either version 3 of the License, or\
 (at your option) any later version."
w = "This program is distributed in the hope that it will be useful,\
 but WITHOUT ANY WARRANTY; without even the implied warranty of\
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the\
 GNU General Public License for more details."

import datetime

# validation function
def validate(n):
    test_1 = 0
    while test_1 is 0:
        try: float(n)
        except ValueError:
            return 0
        else:
            test_1 = 1
            return 1
# not zer0 function
def not0(s):
    test_2 = 0
    while test_2 is 0:
        x = float(s)
        if x == 0:
            return 0
        else:
            test_2 = 1
            return 1
# both
def validatenot0(n):
    test_1 = 0
    while test_1 is 0:
        try: float(n)
        except ValueError:
            return 0
        else:
            test_1 = 1
    while test_1 is 1:
        n_float = float(n)
        if n_float == 0:
            print("No 0 allowed!")
            return 0
        else:
            test_1 = 2
            return 1

#val x > 0
def validategreaterthan0(n):
    test_1 = 0
    while test_1 is 0:
        try: float(n)
        except ValueError:
            return 0
        else:
            test_1 = 1
    while test_1 is 1:
        n_float = float(n)
        if n_float <= 0:
            print("Must be Greater than 0")
            return 0
        else:
            test_1 = 2
            return 1

#save location
fname = 'hist.txt'

vernum = "0.4.1"

#Session time info hist.txt
def beginthesession(fname, version):
    beginses = 0
    while beginses is 0:
        with open(fname, 'a') as f:
            f.write('\n')
            f.write('\n Begin Session: ')
            f.write('{}\n v'.format(str(datetime.datetime.now())))
            f.write('{}\n'.format(version))
        beginses = 1
        
beginthesession(fname, vernum)

#Welcome message
print("Hello there, and welcome to my simple physics calculator")
print("This calculator allows you to plug in your known variables to find another")
print("Type funclist() to show a list of functions")
print("To close the session, type close()")
print("Have fun, and feel free to have a look at the source code, and tweak it if you'd like.")
print("Simplephysicscalc  Copyright (C) 2015  Rory Buchanan\
    This program comes with ABSOLUTELY NO WARRANTY; for details type `show(w)'.\
    This is free software, and you are welcome to redistribute it under certain conditions;\
    type `show(c)' for details.")

def show(details):
    print(details)
    
#save input
def saveInfo(fname, funcname, var1, var2, output1):
    with open(fname, 'a', encoding='utf-8') as f:
        f.write('\n')
        f.write('{}\n'.format(str(datetime.datetime.now())))
        f.write('{}\n'.format(funcname))
        f.write('{}\n'.format(var1))
        f.write('{}\n'.format(var2))
        f.write('{}\n'.format(output1))
        f.write('\n End Function')
        f.write('\n')

#list func
def funclist():
    print("find_force()","find_accel()","find_mass","find_vel","find_disp","close()")
    with open(fname, 'a') as f:
        f.write('\n')
        f.write('{}\n'.format(str(datetime.datetime.now())))
        f.write('\n funclist')
                
# Newtons 2nd (F=ma) derivative equations
# force function F = m * a        
def find_force():
    c = 0
    while c is 0:
        m_str = input("What is the mass of the object? (KG): ")
        if validate(m_str) is 0:
            print("Invalid")
        else:
            c = 1
    c2 = 0
    while c2 is 0:
        a_str = input("What is the acceleration of the object? (ms^-2): ")
        if validate(a_str) is 0:
            print("Invalid")
        else:
            c2 = 1
    m = float(m_str)
    a = float(a_str)
    F = m * a
    funcname = "find_force"
    saveInfo(fname, funcname, m, a, F)
    print(F,"Newtons")
        
# acceleration function a = F / m
def find_accel():
    c = 0
    while c is 0:
        m_str = input("What is the mass of the object? (KG): ")
        if validatenot0(m_str) is 0:
            print("Invalid")
        else:
            c = 1
    c2 = 0
    while c2 is 0:
        F_str = input("What is the force acting on the object? (N): ")
        if validate(F_str) is 0:
            print("Invalid")
        else:
            c2 = 1
    m = float(m_str)
    F = float(F_str)
    a = F / m
    funcname = "find_accel"
    saveInfo(fname, funcname, m, F, a)
    print(a,"ms^-2")
# mass function m = F / a
def find_mass():
    c = 0
    while c is 0:
        a_str = input("What is the acceleration of the object? (ms^-2): ")
        if validatenot0(a_str) is 0:
            print("Invalid")
        else:
            c = 1
    c2 = 0
    while c2 is 0:
        F_str = input("What is the force acting on the object? (N): ")
        if validatenot0(F_str) is 0:
            print("Invalid")
        else:
            c2 = 1
    a = float(a_str)
    F = float(F_str)
    m = F / a
    funcname = "find_mass"
    saveInfo(fname, funcname, a, F, m)
    print(m,"KG")
    
# velocity function v = x / t
def find_vel():
    c = 0
    while c is 0:
        x_str = input("What is the displacement? (m): ")
        if validate(x_str) is 0:
            print("Invalid")
        else:
            c = 1
    c2 = 0
    while c2 is 0:
        t_str = input("What is the time taken? (s): ")
        if validategreaterthan0(t_str) is 0:
            print("Invalid")
        else:
            c2 = 1
    x = float(x_str)
    t = float(t_str)
    v = x / t
    funcname = "find_vel"
    saveInfo(fname, funcname, x, t, v)
    print(v,"ms^-1")

#displacement function x = v * t
def find_disp():
    c = 0
    while c is 0:
        v_str = input("What is the velocity of the object? (ms^-1)")
        if validate(v_str) is 0:
            print("Invalid")
        else:
            c = 1
    c2 = 0
    while c2 is 0:
        t_str = input("What is the time taken? (s): ")
        if validategreaterthan0(t_str) is 0:
            print("Invalid")
        else:
            c2 = 1
    v = float(v_str)
    t = float(t_str)
    x = v / t
    funcname = "find_disp"
    saveInfo(fname, funcname, v, t, x)
    print(x,"m")
# close
def close():
    with open(fname, 'a', encoding='utf-8') as f:
        f.write('\n')
        f.write('{}\n End Session'.format(str(datetime.datetime.now())))
    exit()
