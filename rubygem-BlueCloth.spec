%define	oname	BlueCloth

Summary:	A Ruby implementation of Markdown
Name:		rubygem-%{oname}
Version:	1.0.1
Release:	3
License:	GPLv2+
Group:		Development/Ruby
URL:		https://%{oname}.rubyforge.org/
Source0:	http://gems.rubyforge.org/gems/%{oname}-%{version}.gem
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	ruby-RubyGems
BuildArch:	noarch

%description
BlueCloth is a Ruby implementation of Markdown, a text-to-HTML conversion tool
for web writers. Markdown allows you to write using an easy-to-read,
easy-to-write plain text format, then convert it to structurally valid XHTML
(or HTML).

%prep

%build

%install
rm -rf %{buildroot}
gem install --local --install-dir %{buildroot}/%{ruby_gemdir} --force %{SOURCE0}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%{ruby_gemdir}/cache/%{oname}-%{version}.gem
%{ruby_gemdir}/gems/%{oname}-%{version}
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec



%changelog
* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-2mdv2011.0
+ Revision: 614769
- the mass rebuild of 2010.1 packages

* Wed Feb 03 2010 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.0.1-1mdv2010.1
+ Revision: 500478
- import rubygem-BlueCloth


* Mon Feb  3 2010 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.0.1-1
- initial release
