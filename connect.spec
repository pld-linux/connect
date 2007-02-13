Summary:	Make TCP connection using SOCKS4/5 or HTTPS proxy
Summary(pl.UTF-8):	Tworzenie połączeń TCP poprzez proxy SOCKS4/5 lub HTTPS
Name:		connect
Version:	1.96
Release:	1
License:	GPL v2+
Group:		Applications/Networking
Source0:	http://www.taiyo.co.jp/~gotoh/ssh/connect.c
# NoSource0-md5:	b856937f1cdfca7a3ccfb2fac36ef726
Source1:	http://www.taiyo.co.jp/~gotoh/ssh/connect.html
# NoSource1-md5:	bb972b3a9d435c62023b355960d78f78
URL:		http://www.taiyo.co.jp/~gotoh/ssh/connect.html
Conflicts:	openssh-clients < 2:4.5p1-2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
connect is the simple relaying command to make network connection via
SOCKS and HTTPS proxy. It is mainly intended to be used as "proxy
command" of OpenSSH. You can make SSH session beyond the firewall
with this command.

%description -l pl.UTF-8
connect to proste polecenie przekazujące tworzące połączenie sieciowe
przez proxy SOCKS lub HTTPS. Powstało głównie z myślą o używaniu jako
"proxy command" w OpenSSH. Pozwala nawiązywać sesje SSH zza firewalli.

%prep
%setup -q -c -T

cp %{SOURCE0} %{SOURCE1} .

%build
%{__cc} %{rpmcflags} %{rpmldflags} connect.c -o connect

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install connect $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc connect.html
%attr(755,root,root) %{_bindir}/connect
