#!/usr/bin/env ruby

l = [
     '�ɤ��Ǥ�',
     '�̤�ȴ��',
     '����',
     '���⡼��',
     '�ӥå�',
     '�⤷��',
     '������',
    ]

puts %Q(Content-Type: text/html; charset=EUC-JP

<p>
#{l[rand(l.size)]}����
</p>
<input type="submit" value="�⤦����">
)
