/*
    Galaxy Cosmic Splash Screen for KDE Plasma 6
    SPDX-License-Identifier: GPL-3.0-or-later
*/

import QtQuick
import org.kde.kirigami as Kirigami

Rectangle {
    id: root
    color: "#0B0E17"

    property int stage

    onStageChanged: {
        if (stage === 1) {
            introAnimation.running = true;
        } else if (stage === 2) {
            starsRepeater.opacity = 1.0;
        } else if (stage === 5) {
            fadeOutAnimation.running = true;
        }
    }

    Item {
        id: content
        anchors.fill: parent
        opacity: 0

        // Deep Cosmic Nebula Glow
        Rectangle {
            anchors.centerIn: parent
            width: Math.min(parent.width, parent.height) * 0.9
            height: width
            radius: width / 2
            gradient: Gradient {
                GradientStop { position: 0.0; color: "#4000F0FF" }
                GradientStop { position: 0.4; color: "#2000F0FF" }
                GradientStop { position: 0.7; color: "#10D946EF" }
                GradientStop { position: 1.0; color: "transparent" }
            }
        }

        // Animated Rotating Galaxy Core
        Image {
            id: galaxyLogo
            readonly property real size: Kirigami.Units.gridUnit * 12

            anchors.centerIn: parent
            asynchronous: true
            source: "images/galaxy-core.svg"

            sourceSize.width: size
            sourceSize.height: size

            RotationAnimator on rotation {
                from: 0
                to: 360
                duration: 16000
                loops: Animation.Infinite
                running: true
            }

            SequentialAnimation on scale {
                loops: Animation.Infinite
                running: true
                NumberAnimation { from: 0.95; to: 1.05; duration: 2500; easing.type: Easing.InOutSine }
                NumberAnimation { from: 1.05; to: 0.95; duration: 2500; easing.type: Easing.InOutSine }
            }
        }

        // Orbiting Cosmic Star Indicator
        Item {
            id: busyContainer
            anchors.centerIn: parent
            width: galaxyLogo.width * 1.5
            height: galaxyLogo.height * 1.5

            RotationAnimator on rotation {
                from: 0
                to: 360
                duration: 3500
                loops: Animation.Infinite
                running: true
            }

            Image {
                source: "images/star.svg"
                width: Kirigami.Units.gridUnit * 1.8
                height: width
                anchors.top: parent.top
                anchors.horizontalCenter: parent.horizontalCenter
            }
        }

        // Theme Title & Plasma Brand
        Column {
            anchors {
                bottom: parent.bottom
                horizontalCenter: parent.horizontalCenter
                bottomMargin: Kirigami.Units.gridUnit * 4
            }
            spacing: Kirigami.Units.smallSpacing

            Text {
                anchors.horizontalCenter: parent.horizontalCenter
                color: "#F8FAFC"
                font.pointSize: Kirigami.Theme.defaultFont.pointSize + 4
                font.bold: true
                font.letterSpacing: 2.0
                text: "GALAXY COSMOS"
                textFormat: Text.PlainText
            }

            Text {
                anchors.horizontalCenter: parent.horizontalCenter
                color: "#00F0FF"
                font.pointSize: Kirigami.Theme.defaultFont.pointSize - 1
                font.letterSpacing: 1.2
                text: "KDE Plasma 6"
                textFormat: Text.PlainText
            }
        }
    }

    OpacityAnimator {
        id: introAnimation
        running: true
        target: content
        from: 0
        to: 1
        duration: 1200
        easing.type: Easing.InOutQuad
    }

    OpacityAnimator {
        id: fadeOutAnimation
        running: false
        target: content
        from: 1
        to: 0
        duration: 800
        easing.type: Easing.InOutQuad
    }
}
