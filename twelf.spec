Summary:	meta-theorem proover for LF
Name:		twelf
Version:	1.3
Release:	1
License:	distributable
Group:		Development/Languages
Source0:	http://www.cs.cmu.edu/~%{name}/dist/%{name}-1-3.tar.gz
Source1:	http://www.cs.princeton.edu/~appel/twelf-tutorial/proving.tar
URL:		http://www.cs.cmu.edu/~twelf/
Requires:	smlnj >= 110.0.7
BuildRequires:	smlnj >= 110.0.7
Icon:		twelf-logo.gif

%description
Twelf is an implementation of

 - the LF logical framework, including type reconstruction
 - the Elf constraint logic programming language
 - a meta-theorem prover for LF (very preliminary)
 - an Emacs interface

It also includes a complete User's Guide and example suite; a tutorial
is available from Frank Pfenning <fp@cs.cmu.edu>.  Twelf is written in
Standard ML and uses an inference engine based on explicit
substitutions.  Twelf has been developed at Carnegie Mellon University.

%prep
%setup -n twelf-1-3
tar xf %{SOURCE1}

%build
make

%install
cp doc/info/* $RPM_BUILD_ROOT%{_infodir}
mkdir -p $RPM_BUILD_ROOT%{_libdir}/twelf
cp -rf bin emacs tex $RPM_BUILD_ROOT${_libdir}/twelf
gzip -9nf README

bin/.mkexec /usr/bin/sml %{_libdir}/twelf twelf-server
ln -sf %{_libdir}/twelf/bin/twelf-server $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Wed Oct 18 2000 Roberto Virga <rvirga@cs.princeton.edu> 
- first RPM for release 1.3 (alpha)

%files
%defattr(644,root,root,755)
%doc README.gz examples examples-clp prooving
%dir %{_libdir}/twelf
%dir %{_libdir}/bin
%dir %{_libdir}/bin/.heap
%attr(755,root,root) %{_libdir}/twelf/bin/.heap/twelf*
%attr(755,root,root) %{_libdir}/twelf/bin/.mkexec
%attr(755,root,root) %{_libdir}/twelf/bin/twelf-server
%{_libdir}/twelf/emacs
%{_libdir}/twelf/tex
%{_infodir}/*
