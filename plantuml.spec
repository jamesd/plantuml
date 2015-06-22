Name:           plantuml
Version:        8027
Release:        1%{?dist}
Summary:        Program to generate UML diagram from a text description

License:        LGPLv3+
URL:            http://plantuml.sourceforge.net
Source0:        http://downloads.sourceforge.net/sourceforge/plantuml/plantuml-lgpl-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  jpackage-utils
BuildRequires:  java-devel
BuildRequires:  ant

Requires:       jpackage-utils
Requires:       java-headless

Patch1:         plantuml-doc-errors.patch

%description
PlantUML is a program allowing to draw UML diagrams, using a simple
and human readable text description. It is extremely useful for code
documenting, sketching project architecture during team conversations
and so on.

PlantUML supports the following diagram types
  - sequence diagram
  - use case diagram
  - class diagram
  - activity diagram
  - component diagram
  - state diagram

%package javadoc
Summary:        Javadocs for %{name}
Group:          Documentation
Requires:       jpackage-utils

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -c -n plantuml
%patch1 -p1 -b .doc-errors

%build
ant

# build javadoc
javadoc -d javadoc -sourcepath src net.sourceforge.plantuml

%install
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p %{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%jpackage_script net.sourceforge.plantuml.Run "" "" plantuml plantuml true 

%files
%{_javadir}/%{name}.jar
%{_bindir}/plantuml
%doc README COPYING

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Mon Jun 22 2015 Jan Safranek <jsafrane@redhat.com> - 8027-1
- Update to ver. 8027

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8020-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Mar  6 2015 Jan Safranek <jsafrane@redhat.com> - 8020-1
- Update to ver. 8020

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7992-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Feb 18 2014 Jan Safranek <jsafrane@redhat.com> - 7992-1
- Update to ver. 7992

* Thu Aug 29 2013 Jan Safranek <jsafrane@redhat.com> - 7978-1
- Update to ver. 7978

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7951-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7951-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan 22 2013 Jan Safranek <jsafrane@redhat.com> - 7951-1
- Update to ver. 7951
- Added README and COPYING

* Mon Jan 21 2013 Jan Safranek <jsafrane@redhat.com> - 7950-1
- Update to ver. 7950
- Use plantuml-gpl as source tarball to get source package without bundled
  libraries
  -> use ant
  -> use LGPLv3+ license

* Thu Dec  6 2012 Jan Safranek <jsafrane@redhat.com> - 7943-1
- Package created

