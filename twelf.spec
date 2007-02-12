Summary:	meta-theorem proover for LF
Summary(pl.UTF-8):	Narzędzie do dowodzenia metateorii dla LF
Name:		twelf
Version:	1.3
Release:	2
License:	distributable
Group:		Development/Languages
Source0:	http://www.cs.cmu.edu/~%{name}/dist/%{name}-1-3.tar.gz
# Source0-md5:	90ebfc2dc755d0cec03cccb49c13cdee
Source1:	http://www.cs.princeton.edu/~appel/twelf-tutorial/proving.tar
# Source1-md5:	4c6abab8cd5c9c787c6af8ba4ae81aae
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

%description -l pl.UTF-8
Twelf to implementacja:
 - szkieletu logicznego LF, wraz z rekonstrukcją typów
 - języka programowania logiki Elf
 - dowodzenia meta-teorii dla LF (wstępne)
 - interfejsu do Emacsa.

Ziera także podręcznik użytkownika i przykłady; wprowadzenie jest
dostępne od Franka Pfenninga <fp@cs.cmu.edu>. Twelf jest napisany w
języku Standard ML. Został stworzony w Carnegie Mellon University.

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
%doc README examples examples-clp proving
%dir %{_libdir}/twelf
%dir %{_libdir}/twelf/bin
%dir %{_libdir}/twelf/bin/.heap
%attr(755,root,root) %{_libdir}/twelf/bin/.heap/twelf*
%attr(755,root,root) %{_libdir}/twelf/bin/.mkexec
%attr(755,root,root) %{_libdir}/twelf/bin/twelf-server
%{_libdir}/twelf/emacs
%{_libdir}/twelf/tex
%{_infodir}/*
