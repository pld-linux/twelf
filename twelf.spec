Summary:	meta-theorem proover for LF
Summary(pl):	Narzêdzie do dowodzenia metateorii dla LF
Name:		twelf
Version:	1.3
Release:	2
License:	distributable
Group:		Development/Languages
Group(de):	Entwicklung/Sprachen
Group(pl):	Programowanie/Jêzyki
Source0:	http://www.cs.cmu.edu/~%{name}/dist/%{name}-1-3.tar.gz
Source1:	http://www.cs.princeton.edu/~appel/twelf-tutorial/proving.tar
Icon:		twelf-logo.gif
URL:		http://www.cs.cmu.edu/~twelf/
Requires:	smlnj >= 110.0.7
BuildRequires:	smlnj >= 110.0.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Twelf is an implementation of
 - the LF logical framework, including type reconstruction
 - the Elf constraint logic programming language
 - a meta-theorem prover for LF (very preliminary)
 - an Emacs interface

It also includes a complete User's Guide and example suite; a tutorial
is available from Frank Pfenning <fp@cs.cmu.edu>. Twelf is written in
Standard ML and uses an inference engine based on explicit
substitutions. Twelf has been developed at Carnegie Mellon University.

%description -l pl
Twelf to implementacja:
 - szkieletu logicznego LF, wraz z rekonstrukcj± typów
 - jêzyka programowania logiki Elf
 - dowodzenia meta-teorii dla LF (wstêpne)
 - interfejsu do Emacsa.

Ziera tak¿e podrêcznik u¿ytkownika i przyk³ady; wprowadzenie jest
dostêpne od Franka Pfenninga <fp@cs.cmu.edu>. Twelf jest napisany w
jêzyku Standard ML. Zosta³ stworzony w Carnegie Mellon University.

%prep
%setup -q -n twelf-1-3
tar xf %{SOURCE1}

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_infodir},%{_libdir}/twelf}

install doc/info/* $RPM_BUILD_ROOT%{_infodir}
cp -rf bin emacs tex $RPM_BUILD_ROOT%{_libdir}/twelf
gzip -9nf README

cat > $RPM_BUILD_ROOT%{_libdir}/twelf/bin/twelf-server <<EOF
#!/bin/sh 
/usr/bin/sml-cm \
	@SMLload="%{_libdir}/twelf/bin/.heap/twelf-server" \
	@SMLdebug=/dev/null
EOF

ln -sf %{_libdir}/twelf/bin/twelf-server $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz examples examples-clp proving
%dir %{_libdir}/twelf
%dir %{_libdir}/twelf/bin
%dir %{_libdir}/twelf/bin/.heap
%attr(755,root,root) %{_libdir}/twelf/bin/.heap/twelf*
%attr(755,root,root) %{_libdir}/twelf/bin/.mkexec
%attr(755,root,root) %{_libdir}/twelf/bin/twelf-server
%{_libdir}/twelf/emacs
%{_libdir}/twelf/tex
%{_infodir}/*
