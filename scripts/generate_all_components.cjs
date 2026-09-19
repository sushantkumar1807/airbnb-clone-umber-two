const fs = require('fs');

// Helper to convert HTML string to valid JSX string
function htmlToJsx(html) {
  let jsx = html
    .replace(/<!--[\s\S]*?-->/g, '')
    .replace(/\bclass=/g, 'className=')
    .replace(/\bfor=/g, 'htmlFor=')
    .replace(/\bclip-rule=/g, 'clipRule=')
    .replace(/\bfill-rule=/g, 'fillRule=')
    .replace(/\bstroke-width=/g, 'strokeWidth=')
    .replace(/\bstroke-linecap=/g, 'strokeLinecap=')
    .replace(/\bstroke-linejoin=/g, 'strokeLinejoin=')
    .replace(/\bstroke-miterlimit=/g, 'strokeMiterlimit=')
    .replace(/\bxmlns:xlink=/g, 'xmlnsXlink=')
    .replace(/\bxlink:href=/g, 'xlinkHref=')
    .replace(/<br>/gi, '<br />')
    .replace(/<hr>/gi, '<hr />');

  // Self-close void HTML tags only: img, input
  jsx = jsx.replace(/<(img|input)([^>]*?)(?<!\/)>/gi, '<$1$2 />');

  // Convert inline style strings: style="..." to style={{ ... }}
  jsx = jsx.replace(/style="([^"]*)"/g, (m, styleStr) => {
    const props = styleStr.split(';').filter(p => p.trim());
    const objProps = props.map(p => {
      const parts = p.split(':');
      if (parts.length < 2) return '';
      let key = parts[0].trim();
      let val = parts.slice(1).join(':').trim();
      // camelCase key
      key = key.replace(/-([a-z])/g, (_, c) => c.toUpperCase());
      return `${key}: '${val}'`;
    }).filter(Boolean);
    return `style={{ ${objProps.join(', ')} }}`;
  });

  return jsx;
}

// 1. Header.jsx
const headerHtml = fs.readFileSync('ref_sections/siteHeader.html', 'utf8');
const headerJsx = htmlToJsx(headerHtml);
fs.writeFileSync('src/components/header/Header.jsx', `import React from 'react';

export default function Header() {
  return (
    ${headerJsx}
  );
}
`);
console.log('Header.jsx written.');

// 2. StickyTabs.jsx
const stickyHtml = fs.readFileSync('ref_sections/stickySubnav.html', 'utf8');
let stickyJsx = htmlToJsx(stickyHtml);
// inject state and click handlers
stickyJsx = stickyJsx
  .replace('className="_JXzroy _fTQmRt"', 'className={`_JXzroy ${stickyVisible ? \'_fTQmRt\' : \'\'}`}')
  .replace('aria-hidden="false"', 'aria-hidden={!stickyVisible}')
  .replace('<a href="#photos" data-target="photos">Photos</a>', '<a href="#photos" data-target="photos" className={activeTab === \'photos\' ? \'_KOWlKT\' : \'\'} onClick={(e) => { e.preventDefault(); onTabClick(\'photos\'); }}>Photos</a>')
  .replace('<a href="#amenities" data-target="amenities">Amenities</a>', '<a href="#amenities" data-target="amenities" className={activeTab === \'amenities\' ? \'_KOWlKT\' : \'\'} onClick={(e) => { e.preventDefault(); onTabClick(\'amenities\'); }}>Amenities</a>')
  .replace('<a href="#reviews" data-target="reviews">Reviews</a>', '<a href="#reviews" data-target="reviews" className={activeTab === \'reviews\' ? \'_KOWlKT\' : \'\'} onClick={(e) => { e.preventDefault(); onTabClick(\'reviews\'); }}>Reviews</a>')
  .replace('<a href="#location" data-target="location" className="_KOWlKT">Location</a>', '<a href="#location" data-target="location" className={activeTab === \'location\' ? \'_KOWlKT\' : \'\'} onClick={(e) => { e.preventDefault(); onTabClick(\'location\'); }}>Location</a>')
  .replace('<button className="_NhmiWB _jCniyC" type="button">Reserve</button>', '<button className="_NhmiWB _jCniyC" type="button" onClick={onReserveClick}>Reserve</button>');

fs.writeFileSync('src/components/navigation/StickyTabs.jsx', `import React from 'react';

export default function StickyTabs({ stickyVisible, activeTab, onTabClick, onReserveClick }) {
  return (
    ${stickyJsx}
  );
}
`);
console.log('StickyTabs.jsx written.');

// 3. ListingHeader.jsx
const lhHtml = fs.readFileSync('ref_sections/listingHeader.html', 'utf8');
let lhJsx = htmlToJsx(lhHtml);
lhJsx = lhJsx
  .replace('<button className="_EmrQRK" type="button" id="shareBtn">', '<button className="_EmrQRK" type="button" id="shareBtn" onClick={onShare}>')
  .replace('<button className="_EmrQRK" type="button" id="saveBtn">', '<button className={`_EmrQRK ${isSaved ? \'_nfavct\' : \'\'}`} type="button" id="saveBtn" onClick={onToggleSave}>')
  .replace('<span className="_uOQIyx">Save</span>', '<span className="_uOQIyx">{isSaved ? \'Saved\' : \'Save\'}</span>');

fs.writeFileSync('src/components/listing-header/ListingHeader.jsx', `import React from 'react';

export default function ListingHeader({ onShare, onToggleSave, isSaved }) {
  return (
    ${lhJsx}
  );
}
`);
console.log('ListingHeader.jsx written.');

// 4. GalleryGrid.jsx
const heroHtml = fs.readFileSync('ref_sections/heroGrid.html', 'utf8');
let heroJsx = htmlToJsx(heroHtml);
// inject WebP images & click handlers
heroJsx = heroJsx
  .replace('/assets/images/2367476f-11c4-4a14-a7c6-267be62c1d59.jpeg', '/assets/photos/photo_04_living2.webp')
  .replace('/assets/images/090d8b0b-b539-42c0-84f8-e1fb0cdf9a93.jpeg', '/assets/photos/photo_05_living2.webp')
  .replace('/assets/images/9be71047-fc52-438a-9270-75cb470f6752.jpeg', '/assets/photos/photo_06_living2.webp')
  .replace('/assets/images/67c61c6f-6260-4809-9510-0360e58a345d.jpeg', '/assets/photos/photo_13_bedroom.webp')
  .replace('/assets/images/c904e1ab-a39d-4ef0-bdea-8c0bd16b9e3d.jpeg', '/assets/photos/photo_29_exterior.webp')
  .replace('aria-label="Romantic Jacuzzi 1BHK Candolim | Mirashya UG10 image 1">', 'aria-label="Romantic Jacuzzi 1BHK Candolim | Mirashya UG10 image 1" onClick={() => onPhotoClick(3)}>')
  .replace('aria-label="Romantic Jacuzzi 1BHK Candolim | Mirashya UG10 image 2">', 'aria-label="Romantic Jacuzzi 1BHK Candolim | Mirashya UG10 image 2" onClick={() => onPhotoClick(4)}>')
  .replace('aria-label="Romantic Jacuzzi 1BHK Candolim | Mirashya UG10 image 3">', 'aria-label="Romantic Jacuzzi 1BHK Candolim | Mirashya UG10 image 3" onClick={() => onPhotoClick(5)}>')
  .replace('aria-label="Romantic Jacuzzi 1BHK Candolim | Mirashya UG10 image 4">', 'aria-label="Romantic Jacuzzi 1BHK Candolim | Mirashya UG10 image 4" onClick={() => onPhotoClick(12)}>')
  .replace('aria-label="Romantic Jacuzzi 1BHK Candolim | Mirashya UG10 image 5">', 'aria-label="Romantic Jacuzzi 1BHK Candolim | Mirashya UG10 image 5" onClick={() => onPhotoClick(28)}>')
  .replace('<button className="_ujAXFb" type="button" id="showAllPhotos">', '<button className="_ujAXFb" type="button" id="showAllPhotos" onClick={onShowAllPhotos}>');

fs.writeFileSync('src/components/gallery/GalleryGrid.jsx', `import React from 'react';

export default function GalleryGrid({ onPhotoClick, onShowAllPhotos }) {
  return (
    ${heroJsx}
  );
}
`);
console.log('GalleryGrid.jsx written.');

// 5. Left column breakdown
const contentLeftHtml = fs.readFileSync('ref_sections/contentLeft.html', 'utf8');
// Overview: index 38 to 10824
const overviewHtml = contentLeftHtml.substring(38, 10824).trim();
const overviewJsx = htmlToJsx(overviewHtml);
fs.writeFileSync('src/components/overview/Overview.jsx', `import React from 'react';

export default function Overview() {
  return (
    <>
      ${overviewJsx}
    </>
  );
}
`);
console.log('Overview.jsx written.');

// Highlights: index 10824 to 14536
const highlightsHtml = contentLeftHtml.substring(10824, 14536).trim();
const highlightsJsx = htmlToJsx(highlightsHtml);
fs.writeFileSync('src/components/highlights/Highlights.jsx', `import React from 'react';

export default function Highlights() {
  return (
    ${highlightsJsx}
  );
}
`);
console.log('Highlights.jsx written.');

// Description: index 14536 to 15558
const descHtml = contentLeftHtml.substring(14536, 15558).trim();
let descJsx = htmlToJsx(descHtml);
descJsx = descJsx
  .replace('id="descText" className="_kfKUOt"', 'id="descText" className={isExpanded ? \'\' : \'_kfKUOt\'}')
  .replace('<button className="_yWwrkC" id="descMore">Show more', '<button className="_yWwrkC" id="descMore" onClick={() => setIsExpanded(!isExpanded)}>{isExpanded ? \'Show less\' : \'Show more\'}');

fs.writeFileSync('src/components/description/Description.jsx', `import React, { useState } from 'react';

export default function Description() {
  const [isExpanded, setIsExpanded] = useState(false);
  return (
    ${descJsx}
  );
}
`);
console.log('Description.jsx written.');

// Sleep: index 15558 to 16003
const sleepHtml = contentLeftHtml.substring(15558, 16003).trim();
let sleepJsx = htmlToJsx(sleepHtml);
sleepJsx = sleepJsx
  .replace('/assets/images/67c61c6f-6260-4809-9510-0360e58a345d.jpeg', '/assets/photos/photo_13_bedroom.webp')
  .replace('/assets/images/a9831aeb-f441-44f5-a38f-4cf54e3f0fcf.jpeg', '/assets/photos/photo_01_living1.webp');

fs.writeFileSync('src/components/sleep/SleepingArrangements.jsx', `import React from 'react';

export default function SleepingArrangements() {
  return (
    ${sleepJsx}
  );
}
`);
console.log('SleepingArrangements.jsx written.');

// Amenities: index 16003 to 25435
const amenHtml = contentLeftHtml.substring(16003, 25435).trim();
let amenJsx = htmlToJsx(amenHtml);
amenJsx = amenJsx.replace('<button className="_XZuuKk" id="showAmen">', '<button className="_XZuuKk" id="showAmen" onClick={onShowAllAmenities}>');
fs.writeFileSync('src/components/amenities/Amenities.jsx', `import React from 'react';

export default function Amenities({ onShowAllAmenities }) {
  return (
    ${amenJsx}
  );
}
`);
console.log('Amenities.jsx written.');

// Calendar: index 25435 to end
const calHtml = contentLeftHtml.substring(25435).trim();
let calJsx = htmlToJsx(calHtml);
calJsx = calJsx.replace('<button className="_WKAkzo">Clear dates</button>', '<button className="_WKAkzo" onClick={onClearDates}>Clear dates</button>');
fs.writeFileSync('src/components/calendar/CalendarSection.jsx', `import React from 'react';

export default function CalendarSection({ onClearDates }) {
  return (
    ${calJsx}
  );
}
`);
console.log('CalendarSection.jsx written.');

// 6. BookingCard.jsx
const bookingHtml = fs.readFileSync('ref_sections/bookingSticky.html', 'utf8');
let bookingJsx = htmlToJsx(bookingHtml);
bookingJsx = bookingJsx
  .replace('<button className="_Spojam" type="button">Claim</button>', '<button className="_Spojam" type="button" onClick={onClaimDiscount}>Claim</button>')
  .replace('<button className="_NhmiWB _YkNyTO" type="button" id="reserveBtn">Reserve</button>', '<button className="_NhmiWB _YkNyTO" type="button" id="reserveBtn" onClick={onReserve}>Reserve</button>')
  .replace('<a href="#">Report this listing</a>', '<a href="#" onClick={(e) => { e.preventDefault(); onReport(); }}>Report this listing</a>');

fs.writeFileSync('src/components/booking/BookingCard.jsx', `import React from 'react';

export default function BookingCard({ onReserve, onClaimDiscount, onReport }) {
  return (
    ${bookingJsx}
  );
}
`);
console.log('BookingCard.jsx written.');

// 7. Reviews.jsx
const revHtml = fs.readFileSync('ref_sections/reviews.html', 'utf8');
let revJsx = htmlToJsx(revHtml);
revJsx = revJsx.replace('<button className="_XZuuKk">Show all 19 reviews</button>', '<button className="_XZuuKk" onClick={onShowAllReviews}>Show all 19 reviews</button>');
fs.writeFileSync('src/components/reviews/Reviews.jsx', `import React from 'react';

export default function Reviews({ onShowAllReviews }) {
  return (
    ${revJsx}
  );
}
`);
console.log('Reviews.jsx written.');

// 8. locationAndWide.html breakdown:
const locHtml = fs.readFileSync('ref_sections/locationAndWide.html', 'utf8');
// location: 0 to 2582
const locationPart = locHtml.substring(0, 2582).trim();
const locationJsx = htmlToJsx(locationPart);
fs.writeFileSync('src/components/location/LocationMap.jsx', `import React, { useState } from 'react';

export default function LocationMap() {
  const [showMore, setShowMore] = useState(false);
  return (
    ${locationJsx}
  );
}
`);
console.log('LocationMap.jsx written.');

// hostSection: 2582 to 6481
const hostPart = locHtml.substring(2582, 6481).trim();
let hostJsx = htmlToJsx(hostPart);
hostJsx = hostJsx.replace('<button className="_egLfkO">Message host</button>', '<button className="_egLfkO" onClick={onMessageHost}>Message host</button>');
fs.writeFileSync('src/components/host/HostSection.jsx', `import React from 'react';

export default function HostSection({ onMessageHost }) {
  return (
    ${hostJsx}
  );
}
`);
console.log('HostSection.jsx written.');

// thingsToKnow: 6481 to 9231
const ttkPart = locHtml.substring(6481, 9231).trim();
const ttkJsx = htmlToJsx(ttkPart);
fs.writeFileSync('src/components/things-to-know/ThingsToKnow.jsx', `import React from 'react';

export default function ThingsToKnow() {
  return (
    ${ttkJsx}
  );
}
`);
console.log('ThingsToKnow.jsx written.');

// nearby: 9231 to end
let nearbyPart = locHtml.substring(9231).trim();
nearbyPart = nearbyPart.replace(/<\/main>[\s\S]*$/, '').replace(/<\/div>\s*<\/div>\s*$/, '');
let nearbyJsx = htmlToJsx(nearbyPart);
// add carousel click handlers
nearbyJsx = nearbyJsx
  .replace('id="simPrev" disabled=""', 'id="simPrev" disabled={currentPage === 1} onClick={handlePrev}')
  .replace('id="simNext"', 'id="simNext" disabled={currentPage === 2} onClick={handleNext}')
  .replace('<span className="_klVRbI">1 / 2</span>', '<span className="_klVRbI">{currentPage} / 2</span>');

fs.writeFileSync('src/components/nearby/NearbyStays.jsx', `import React, { useState, useRef } from 'react';

export default function NearbyStays() {
  const [currentPage, setCurrentPage] = useState(1);
  const trackRef = useRef(null);

  const handlePrev = () => {
    if (trackRef.current) {
      trackRef.current.scrollBy({ left: -600, behavior: 'smooth' });
    }
    setCurrentPage(1);
  };

  const handleNext = () => {
    if (trackRef.current) {
      trackRef.current.scrollBy({ left: 600, behavior: 'smooth' });
    }
    setCurrentPage(2);
  };

  return (
    ${nearbyJsx}
  );
}
`);
console.log('NearbyStays.jsx written.');

// 9. AmenitiesModal.jsx
const amenModalHtml = fs.readFileSync('ref_sections/amenModal.html', 'utf8');
let amenModalJsx = htmlToJsx(amenModalHtml);
amenModalJsx = amenModalJsx
  .replace('className="_yBjuYG" id="amenModal" aria-hidden="true"', 'className={`_yBjuYG ${isOpen ? \'_PjnNJs\' : \'\'}`} id="amenModal" aria-hidden={!isOpen}')
  .replace('<button className="_bNHEUf _cqnRCd" type="button" aria-label="Close" id="amenClose">', '<button className="_bNHEUf _cqnRCd" type="button" aria-label="Close" id="amenClose" onClick={onClose}>');

fs.writeFileSync('src/components/amenities/AmenitiesModal.jsx', `import React, { useEffect } from 'react';

export default function AmenitiesModal({ isOpen, onClose }) {
  useEffect(() => {
    if (isOpen) {
      document.body.classList.add('_pINcte');
      const handleKeyDown = (e) => {
        if (e.key === 'Escape') onClose();
      };
      window.addEventListener('keydown', handleKeyDown);
      return () => {
        document.body.classList.remove('_pINcte');
        window.removeEventListener('keydown', handleKeyDown);
      };
    }
  }, [isOpen, onClose]);

  if (!isOpen) return null;

  return (
    ${amenModalJsx}
  );
}
`);
console.log('AmenitiesModal.jsx written.');

// 10. LightboxModal.jsx
const lbHtml = fs.readFileSync('ref_sections/lightboxModal.html', 'utf8');
let lbJsx = htmlToJsx(lbHtml);
// inject state & handlers
lbJsx = lbJsx
  .replace('className="_zFbfbh" id="lightbox" aria-hidden="true"', 'className={`_zFbfbh ${isOpen ? \'_PjnNJs\' : \'\'}`} id="lightbox" aria-hidden={!isOpen}')
  .replace('id="lbGrid">', 'id="lbGrid" onClick={onGridClick}>')
  .replace('<div className="_QIemms" id="lbTitle"></div>', '<div className="_QIemms" id="lbTitle">{categoryName}</div>')
  .replace('<span className="_iRDAKc" id="lbCounter"></span>', '<span className="_iRDAKc" id="lbCounter">{currentIndex + 1} / {totalPhotos}</span>')
  .replace('id="lbClose">', 'id="lbClose" onClick={onClose}>')
  .replace('id="lbPrev" disabled="">', 'id="lbPrev" disabled={currentIndex === 0} onClick={onPrev}>')
  .replace('id="lbNext" disabled="">', 'id="lbNext" disabled={currentIndex === totalPhotos - 1} onClick={onNext}>')
  .replace('<div className="_VPKRNC" id="lbStage"></div>', '<div className="_VPKRNC" id="lbStage"><img key={currentIndex} className="_SSnzPz" src={currentPhotoSrc} alt={categoryName} /></div>');

fs.writeFileSync('src/components/lightbox/LightboxModal.jsx', `import React, { useEffect } from 'react';

export default function LightboxModal({
  isOpen,
  currentIndex,
  totalPhotos,
  categoryName,
  currentPhotoSrc,
  onClose,
  onGridClick,
  onPrev,
  onNext
}) {
  useEffect(() => {
    if (!isOpen) return;
    document.body.classList.add('_pINcte');
    const handleKey = (e) => {
      if (e.key === 'Escape') onClose();
      if (e.key === 'ArrowLeft') onPrev();
      if (e.key === 'ArrowRight') onNext();
    };
    window.addEventListener('keydown', handleKey);
    return () => {
      document.body.classList.remove('_pINcte');
      window.removeEventListener('keydown', handleKey);
    };
  }, [isOpen, onClose, onPrev, onNext]);

  if (!isOpen) return null;

  return (
    ${lbJsx}
  );
}
`);
console.log('LightboxModal.jsx written.');

// 11. PhotoTourModal.jsx
const tourHtml = fs.readFileSync('ref_sections/photoTourModal.html', 'utf8');
let tourJsx = htmlToJsx(tourHtml);
// inject state & handlers
tourJsx = tourJsx
  .replace('className="_KpcKWX" id="_KpcKWX" aria-hidden="true"', 'className={`_KpcKWX ${isOpen ? \'_PjnNJs\' : \'\'}`} id="_KpcKWX" aria-hidden={!isOpen}')
  .replace('id="tourBack">', 'id="tourBack" onClick={onClose}>')
  .replace(/<button className="_GXrMIo" type="button" data-idx="(\d+)"/g, '<button className="_GXrMIo" type="button" data-idx="$1" onClick={() => onPhotoClick($1)}');

fs.writeFileSync('src/components/photo-tour/PhotoTourModal.jsx', `import React, { useEffect } from 'react';

export default function PhotoTourModal({ isOpen, onClose, onPhotoClick, onShare, onSave }) {
  useEffect(() => {
    if (!isOpen) return;
    document.body.classList.add('_pINcte');
    const handleKey = (e) => {
      if (e.key === 'Escape') onClose();
    };
    window.addEventListener('keydown', handleKey);
    return () => {
      document.body.classList.remove('_pINcte');
      window.removeEventListener('keydown', handleKey);
    };
  }, [isOpen, onClose]);

  const scrollToRoom = (id) => {
    const el = document.getElementById(id);
    if (el) el.scrollIntoView({ behavior: 'smooth' });
  };

  if (!isOpen) return null;

  return (
    ${tourJsx}
  );
}
`);
console.log('PhotoTourModal.jsx written.');

// 12. Toast.jsx
fs.writeFileSync('src/components/common/Toast.jsx', `import React from 'react';

export default function Toast({ text, visible }) {
  return (
    <div className={\`_HALoyX \${visible ? '_fTQmRt' : ''}\`} id="_HALoyX">
      {text}
    </div>
  );
}
`);
console.log('Toast.jsx written.');
