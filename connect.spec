Summary:	Make TCP connection using SOCKS4/5 or HTTPS proxy
Summary(pl.UTF-8):	Tworzenie połączeń TCP poprzez proxy SOCKS4/5 lub HTTPS
Name:		connect
Version:	1.96
Release:	3
License:	GPL v2+
Group:		Applications/Networking
Source0:	http://www.taiyo.co.jp/~gotoh/ssh/%{name}.c
# NoSource0-md5:	b856937f1cdfca7a3ccfb2fac36ef726
Source1:	http://www.taiyo.co.jp/~gotoh/ssh/%{name}.html
# NoSource1-md5:	bb972b3a9d435c62023b355960d78f78
URL:		http://bent.latency.net/bent/git/goto-san-connect-1.85/src/connect.html
Conflicts:	openssh-clients < 2:4.5p1-2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
connect is the simple relaying command to make network connection via
SOCKS and HTTPS proxy. It is mainly intended to be used as "proxy
command" of OpenSSH. You can make SSH session beyond the firewall with
this command.

NOTE: Since OpenSSH 5.4 you can use ssh -W option for plain TCP
tunnel: ProxyCommand ssh -q -W %h:%p gateway.example.com

%description -l pl.UTF-8
connect to proste polecenie przekazujące tworzące połączenie sieciowe
przez proxy SOCKS lub HTTPS. Powstało głównie z myślą o używaniu jako
"proxy command" w OpenSSH. Pozwala nawiązywać sesje SSH zza firewalli.

%prep
%setup -q -c -T
cp -p %{SOURCE0} %{SOURCE1} .

%build
%{__cc} %{rpmcflags} %{rpmldflags} connect.c -o connect

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -p connect $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc connect.html
%attr(755,root,root) %{_bindir}/connect
