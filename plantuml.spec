Name:           plantuml
Version:        8033
Release:        7%{?dist}
Summary:        Program to generate UML diagram from a text description

License:        LGPLv3+
URL:            http://plantuml.com/
Source0:        http://downloads.sourceforge.net/plantuml/%{name}-lgpl-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  ant
BuildRequires:  javapackages-local

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
Summary:        Javadoc for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -c -n plantuml

# Convert from dos to unix line ending
sed -i.orig 's|\r||g' README
touch -r README.orig README
rm README.orig

%build

ant

# build javadoc
%javadoc -encoding UTF-8 -Xdoclint:none -classpath %{name}.jar -d javadoc $(find src -name "*.java") -windowtitle "PlantUML %{version}"

%install
# Set jar location
%mvn_file net.sourceforge.%{name}:%{name} %{name}
# Configure maven depmap
%mvn_artifact net.sourceforge.%{name}:%{name}:%{version} %{name}.jar
%mvn_install -J javadoc

%jpackage_script net.sourceforge.plantuml.Run "" "" plantuml plantuml true

%files -f .mfiles
%{_bindir}/plantuml
%doc README
%license COPYING

%files javadoc -f .mfiles-javadoc
%license COPYING

%changelog
* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8033-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8033-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8033-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 8033-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Nov 26 2015 gil cattaneo <puntogil@libero.it> 8033-3
- edited javadoc task

* Thu Nov 26 2015 gil cattaneo <puntogil@libero.it> 8033-2
- fix README line ending

* Thu Nov 26 2015 gil cattaneo <puntogil@libero.it> 8033-1
- update to 8033
- minor changes to adapt to current guideline
- resolve some rpmlint problems
- introduce license macro
- fix java8doc doclint problems
- add maven metadata

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

